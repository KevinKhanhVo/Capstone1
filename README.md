# Trainers interactions with Pokemons

## Overview
A website where users can view categories of pokemons filtered by generations. Users are able to select a pokemon to see detailed information on their base stats, locations and list of movesets. Users can sign up to create a trainer profile and to catch pokemons. Pokemons that are caught will have 5 moves randomly selected from their movesets. Trainers are able to release the pokemons back to the wild and to select new ones. Trainers will see the first 6 pokemons as their main pokemons.

## Tech Stack
Python, Flask, WTForms, SQLAlchemy, PostgreSQL, JavaScript

## API
https://pokeapi.co/

## Sensitive Information
Passwords are secured using Flask Bcrypt. Users are able to view the pokedex and pokemon details, however users cannot add pokemons to their team if they have not signed up.

## Long Term Goals for Additional Features
* Implementation of Pokemon battle system between trainers and their current pokemons.
* Implementation of gym battles.
* Implementation of gym badges.
* Keep records of wins and losses for all battles. 
* Keep records of gym attempts. 
