from app import db, create_app  # Import db and create_app from app
from app.models import Hero, Power, HeroPower

def seed_data():
    app = create_app()  # Create an instance of the Flask app
    with app.app_context():  
       
        HeroPower.query.delete()
        Power.query.delete()
        Hero.query.delete()
        
        # Create heroes
        hero1 = Hero(name='Bruce Wayne', super_name='Batman')
        hero2 = Hero(name='Clark Kent', super_name='Superman')
        hero3 = Hero(name='Diana Prince', super_name='Wonder Woman')
        
        # Create powers with names and descriptions
        power1 = Power(name='Flight', description='Allows the hero to fly at supersonic speeds.')
        power2 = Power(name='Super Strength', description='Gives the hero super-human strength.')
        power3 = Power(name='Martial Arts', description='Mastery of hand-to-hand combat and martial arts techniques.')
        
        # Add relationships (HeroPower)
        hero_power1 = HeroPower(hero=hero1, power=power3, strength='Strong')
        hero_power2 = HeroPower(hero=hero2, power=power1, strength='Strong')
        hero_power3 = HeroPower(hero=hero2, power=power2, strength='Strong')
        hero_power4 = HeroPower(hero=hero3, power=power2, strength='Strong')
        
        # Add objects to the session
        db.session.add_all([hero1, hero2, hero3])
        db.session.add_all([power1, power2, power3])
        db.session.add_all([hero_power1, hero_power2, hero_power3, hero_power4])
        
        
        db.session.commit()
        print("Data seeded successfully!")

if __name__ == '__main__':
    seed_data()
