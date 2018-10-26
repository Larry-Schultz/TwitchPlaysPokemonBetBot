# twitchPlaysPokemonBetBot

This is an application I wrote around 3 years ago that performed all operations necesary to act as a Betting AI for the Pokemon Stadium mode of Twitch Plays Pokemon.

It has algorithms to determine what pokemon to bet on based on the current bets of current users, the success rates of those users, handles suspected actors using similar algorithms and uses code found elsewhere to predict pokemon matchups.

The application also handles the direction votes, Who's That Pokemon? and has chatbot functionality using markov chains based on input from the TwitchPlaysPokemon channel.

The application stores data in a Postgres database I had on my local machine for betting historical data.  Showing the wins and loses of each player, and pulling data from a remote source.
