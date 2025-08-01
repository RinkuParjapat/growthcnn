from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from leads.models import Base, Lead

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def create_lead(name, email, phone, source):
    session = Session()
    new_lead = Lead(name=name, email=email, phone=phone, source=source)
    session.add(new_lead)
    session.commit()
    session.close()
    return new_lead

def get_all_leads():
    session = Session()
    leads = session.query(Lead).all()
    session.close()
    return leads

def update_stage(lead_id, new_stage):
    session = Session()
    lead = session.query(Lead).get(lead_id)
    if lead:
        lead.stage = new_stage
        session.commit()
    session.close()

def delete_lead(lead_id):
    session = Session()
    lead = session.query(Lead).get(lead_id)
    if lead:
        session.delete(lead)
        session.commit()
    session.close()
