#order details model
from app.app import db
from app.models.usermodel import User

class OrderDetails(db.Document):
	itemname = db.StringField(required=True)
	distributer = db.StringField(required=True)
	ordereduser = db.ReferenceField(User)
	statusoforder = db.StringField(default="Pending Pickup")
	orderid = db.StringField(required=True)
	deliveryaddress = db.StringField(required=True)
	cost = db.StringField(required=True)