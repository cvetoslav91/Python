import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Import your models here


# Create queries within functions
def create_pet(name, species):
    Pet.objects.create(name=name, species=species)
    return f"{name} is a very cute {species}!"


def create_artifact(name, origin, age, description, is_magical):
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    result = []
    for location in Location.objects.all().order_by('-id'):
        result.append(f'{location.name} has a population of {location.population}!')
    return '\n'.join(result)


def new_capital():
    new_capital_location = Location.objects.first()
    new_capital_location.is_capital = True
    new_capital_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    for car in Car.objects.all():
        discount = sum([int(digit) for digit in str(car.year)]) / 100
        car.price_with_discount = float(car.price) - (float(car.price) * discount)
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    result = []
    for task in Task.objects.filter(is_finished=False):
        result.append(f'Task - {task.title} needs to be done until {task.due_date}!')
    return '\n'.join(result)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 == 1:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    for task in Task.objects.filter(title=task_title):
        task.description = ''.join([chr(ord(c) - 3) for c in text])
        task.save()


def get_deluxe_rooms():
    result = []
    for room in HotelRoom.objects.filter(room_type='Deluxe'):
        if room.id % 2 == 0:
            result.append(f'Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!')
    return '\n'.join(result)


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all().order_by('id')

    for i in range(len(all_rooms)):
        current_room = all_rooms[i]
        if current_room.is_reserved:
            if i == 0:
                current_room.capacity += current_room.capacity
                current_room.save()
            else:
                previous_room = all_rooms[i - 1]
                current_room.capacity += previous_room.capacity
                current_room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if not last_room.is_reserved:
        last_room.delete()


def update_characters():
    for character in Character.objects.all():
        if character.class_name == 'Mage':
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == 'Warrior':
            character.hit_points /= 2
            character.dexterity += 4
        elif character.class_name == 'Assassin' or character.class_name == 'Scout':
            character.inventory = 'The inventory is empty'
        character.save()


def fuse_characters(first_character: Character, second_character: Character):
    new_character = Character(
        name=f"{first_character.name} {second_character.name}",
        class_name='Fusion',
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=''
    )

    if first_character.class_name == 'Mage' or first_character.class_name == 'Scout':
        new_character.inventory = f"Bow of the Elven Lords, Amulet of Eternal Wisdom"
    if first_character.class_name == 'Warrior' or first_character.class_name == 'Assassin':
        new_character.inventory = f"Dragon Scale Armor, Excalibur"
    new_character.save()

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    for character in Character.objects.all():
        character.dexterity = 30
        character.save()


def grand_intelligence():
    for character in Character.objects.all():
        character.intelligence = 40
        character.save()


def grand_strength():
    for character in Character.objects.all():
        character.strength = 50
        character.save()


def delete_characters():
    for character in Character.objects.all():
        if character.inventory == "The inventory is empty":
            character.delete()

