all:
	docker-compose up --build

clean:
	docker-compose down

fclean: clean
	docker system prune -af

re: fclean all

.PHONY: all clean fclean re