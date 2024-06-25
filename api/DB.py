import random
from typing import List
from models.models import Cupcake

allowed_types = ["Always Available", "Holidays", "Special Events", "Custom"]

cupcakes: List[Cupcake] = [
    Cupcake(id=1, name="Vanilla Dream", description="Light and fluffy vanilla cupcake with vanilla buttercream frosting", type=random.choice(allowed_types), price=3.50, image="https://www.torontocupcake.com/images/cupcakes_flavours/chocolatehazelnut.webp"),
    Cupcake(id=2, name="Chocolate Decadence", description="Rich and moist chocolate cupcake with chocolate ganache frosting", type=random.choice(allowed_types), price=4.00, image="https://www.torontocupcake.com/images/cupcakes_flavours/chocolatehazelnut.webp"),
    Cupcake(id=3, name="Red Velvet Delight", description="Velvety red velvet cupcake with cream cheese frosting", type=random.choice(allowed_types), price=3.75, image="https://www.torontocupcake.com/images/cupcakes_flavours/chocolatechocolate.webp"),
    Cupcake(id=4, name="Strawberry Surprise", description="Vanilla cupcake with fresh strawberry filling and whipped cream frosting", type=random.choice(allowed_types), price=4.25, image="https://www.torontocupcake.com/images/cupcakes_flavours/vanillachocolateganache.webp"),
    Cupcake(id=5, name="Lemon Zest", description="Tangy lemon cupcake with lemon glaze", type=random.choice(allowed_types), price=3.00, image="https://www.torontocupcake.com/images/cupcakes_flavours/hotfudgesundae.webp"),
]