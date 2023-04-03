import os

class Config:
    
    # DB settings
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost:5432/db_feedback_app'

    # App settings
    ## Metadata 
    DESCRIPTION = '''
    Feedback-functionality webapp is a simple backend service to store the feedback provided by our users of our products.
    '''

    TAGS_METADATA = [
        {
            "name": "Feedback",
            "description": "Operations with the feedbacks.",
        }
    ]

    TITLE="Feedback App"
    VERSION="0.0.1"
    CONTACT={
            "name": "DAguirreAg",
            "url": "https://github.com/DAguirreAg/"
            }
    LICENSE_INFO={
                "name": " MIT License",
                "url": "https://mit-license.org/",
                }