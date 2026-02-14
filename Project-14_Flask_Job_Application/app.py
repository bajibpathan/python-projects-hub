import os
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

# =====================================================
# Application Configuration
# =====================================================

app = Flask(__name__)

# Load sensitive data from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev_key")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Mail Configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)


# =====================================================
# Database Model
# =====================================================

class Form(db.Model):
    """
    Database model representing a job application form.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    occupation = db.Column(db.String(80), nullable=False)


# =====================================================
# Routes
# =====================================================

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route for displaying and processing the form.
    """

    if request.method == "POST":
        try:
            # Retrieve form data
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            email = request.form.get("email")
            date = request.form.get("date")
            occupation = request.form.get("occupation")

            # Validate input
            if not all([first_name, last_name, email, date, occupation]):
                flash("All fields are required.", "danger")
                return redirect(url_for("index"))

            date_obj = datetime.strptime(date, "%Y-%m-%d")

            # Save to database
            form = Form(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date_obj,
                occupation=occupation
            )

            db.session.add(form)
            db.session.commit()

            # Send confirmation email
            message_body = (
                f"Dear {first_name},\n\n"
                "Thank you for your job application.\n\n"
                f"Name: {first_name} {last_name}\n"
                f"Start Date: {date}\n"
                f"Occupation: {occupation}\n\n"
                "We will contact you soon.\n"
                "Best regards."
            )

            message = Message(
                subject="Job Application Confirmation",
                sender=app.config["MAIL_USERNAME"],
                recipients=[email],
                body=message_body
            )

            mail.send(message)

            flash("Your application was submitted successfully!", "success")
            return redirect(url_for("index"))

        except Exception as e:
            db.session.rollback()
            flash("An error occurred while processing your request.", "danger")
            print(f"Error: {e}")
            return redirect(url_for("index"))

    return render_template("index.html")


# =====================================================
# Application Entry Point
# =====================================================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5001)
