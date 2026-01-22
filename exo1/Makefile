# Lance le conteneur 
all:
	docker-compose up --build

# Arrête tout
clean:
	docker-compose down

# Nettoie tout (images incluses)
fclean: clean
	docker system prune -af

# Relance propre
re: fclean all

.PHONY: all clean fclean re