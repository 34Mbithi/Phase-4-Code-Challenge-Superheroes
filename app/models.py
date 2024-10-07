from app import db

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(50), nullable=False)
    
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name
        }

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    strength = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength
        }
    
    @staticmethod
    def validate_strength(value):
        allowed_strengths = ['Strong', 'Weak', 'Average']
        if value not in allowed_strengths:
            raise ValueError(f"Strength must be one of: {', '.join(allowed_strengths)}")