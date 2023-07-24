import discord
import random

# Remplacez "YOUR_TOKEN_HERE" par le véritable token de votre bot Discord.
TOKEN = "MTEzMjk2ODcwMjc5MTM4OTI5NA.G0nCHA.O4eohwJbKTeFkso2VL3MYKzhsD0-0AU7jJ98Ac"

client = discord.Client()

# Liste des questions nintendo. Chaque question est un dictionnaire avec les clés "question", "choices" et "answer".
nintendo_questions = [
    {
        "question": "Quel personnage emblématique de Nintendo est un plombier italien ?",
        "choices": ["a) Link", "b) Mario", "c) Pikachu", "d) Donkey Kong"],
        "answer": "b) Mario"
    },
    {
        "question": "Quel est le nom de la célèbre princesse de la série de jeux Super Mario ?",
        "choices": ["a) Daisy", "b) Peach", "c) Zelda", "d) Samus"],
        "answer": "b) Peach"
    },
    {
        "question": "Dans quelle série de jeux de combat de Nintendo pouvez-vous retrouver des personnages tels que Kirby, Mario, et Pikachu ?",
        "choices": ["a) Super Smash Bros", "b) Street Fighter", "c) Tekken", "d) Mortal Kombat"],
        "answer": "a) Super Smash Bros"
    },
    {
        "question": "Quel est le nom du célèbre jeu de simulation de vie de Nintendo, où vous incarnez un personnage vivant dans un village rempli d'animaux anthropomorphes ?",
        "choices": ["a) Animal Crossing", "b) Harvest Moon", "c) Stardew Valley", "d) The Sims"],
        "answer": "a) Animal Crossing"
    },
    {
        "question": "Quel est le nom du célèbre personnage de Nintendo qui voyage à travers le Royaume Champignon pour sauver la princesse Peach des griffes de Bowser ?",
        "choices": ["a) Luigi", "b) Yoshi", "c) Toad", "d) Mario"],
        "answer": "d) Mario"
    },
    {
        "question": "Quel est le nom du royaume dans lequel se déroule la majorité de l'action dans le jeu -The Legend of Zelda: Breath of the Wild- ?",
        "choices": ["a) Hyrule", "b) Mushroom Kingdom", "c) Termina", "d) Isle Delfino"],
        "answer": "a) Hyrule"
    },
    {
        "question": "Dans le jeu -Super Mario 64-, combien d'étoiles sont dissimulées dans le château de Peach, que Mario doit collecter pour terminer le jeu ?",
        "choices": ["a) 100", "b) 120", "c) 150", "d) 64"],
        "answer": "b) 120"
    },
    {
        "question": "Quel est le nom du vaisseau spatial piloté par Fox McCloud dans la série de jeux -Star Fox- ?",
        "choices": ["a) Odyssey", "b) Falcon", "c) Arwing", "d) Starfire"],
        "answer": "c) Arwing"
    },
    {
        "question": "Dans le jeu -Metroid Prime-, quel est le nom de l'héroïne intergalactique qui se bat contre les Space Pirates et les Métroïdes ?",
        "choices": ["a) Samus Aran", "b) Lara Croft", "c) Jill Valentine", "d) Princess Peach"],
        "answer": "a) Samus Aran"
    },
    {
        "question": "Combien de Pokémon originaux étaient disponibles dans le Pokédex national de la première génération de jeux Pokémon (Rouge, Bleu, Vert et Jaune) ?",
        "choices": ["a) 150", "b) 151", "c) 200", "d) 100"],
        "answer": "b) 151"
    },
    # Ajoutez plus de questions ici
]

# Classement des joueurs avec leurs scores.
player_scores = {}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!nintendo'):
        await handle_nintendo(message)
    elif message.content.startswith('!stats'):
        await show_stats(message)
    elif message.content.startswith('!help'):
        await show_help(message)

async def handle_nintendo(message):
    game = random.choice(nintendo_questions)

    # Envoie le jeu choisi au canal.
    await message.channel.send(f"Question Nintendo aléatoire : {game}")

async def show_stats(message):
    user_score = player_scores.get(message.author.id, 0)
    await message.channel.send(f"Votre score actuel est de {user_score} points.")


async def show_help(message):
    help_embed = discord.Embed(title="Aide - QuizzyNintendo", description="Voici les différentes commandes disponibles :", color=discord.Color.green())
    help_embed.add_field(name="!nintendo", value="Démarre une session de quiz avec des questions de QuizzyNintendo.", inline=False)
    help_embed.add_field(name="!stats", value="Affiche votre score actuel.", inline=False)
    help_embed.add_field(name="!help", value="Affiche cette aide.", inline=False)
    await message.channel.send(embed=help_embed)

# Connectez-vous au serveur Discord avec le token du bot.
client.run(TOKEN)
