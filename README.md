# ft_transcendence

The `ft_transcendence` is the final project of the 42 curriculum, focusing on the design, development, and organization of a full-stack web application. This project involves building a comprehensive website that hosts a Pong competition, allowing users to play Pong with each other in real-time.

<img src="https://github.com/dardangerguri/ft_transcendence/blob/main/ft_transcendence.gif" alt="ft_transcendence"/>

## About the project

`Call of Pong` is a Pong game that allows players to compete in 1v1 matches or tournaments, either online by creating an account or locally without saving any data. Additionally, players can challenge an AI in a single-player mode.

The frontend of the game is developed using pure vanilla JavaScript, ensuring a lightweight and fast-performing interface without relying on external frameworks. The backend is powered by the Django framework, providing a robust and scalable server-side architecture for managing user data and game logic.

The website is designed as a single-page application, and users can utilize the Back and Forward buttons of their browser to navigate through the application.

To simplify deployment, the entire application is containerized using Docker. Everything can be launched with a single command to run an autonomous container.


### Modules


- **Backend Framework:** Utilize the Django REST framework to provide a robust and scalable backend, enabling seamless data handling and API endpoints.

- **Database:** Employ PostgreSQL for consistent and reliable data management, ensuring efficient storage and retrieval of player and game information.

- **User Management and Authentication:** Implement secure user authentication and management features, including unique profiles.

- **Remote Gameplay:** Enable players to compete in real-time across different devices through remote multiplayer functionality.

- **Live Chat:** Integrate a chat system allowing users to send messages, block others, invite players to games, and receive tournament notifications.

- **AI Opponent:** Introduce an AI player with challenging gameplay dynamics, simulating human behaviores.

- **Microservices Architecture:** Design the backend as loosely coupled microservices for improved scalability, maintainability, and independent deployment of features.

- **Server-Side Pong API:** Transition the game logic to the server side, developing an API to facilitate gameplay via both web interfaces and command-line interactions.

- **CLI vs Web Gameplay:** Enable gameplay through a Command-Line Interface (CLI).

- **Game Customization Options:** Offer various customization features for enhanced gameplay settings, giving players flexibility in their experience.

- **Browser Compatibility:** Expand the website's compatibility to ensure smooth functionality across multiple browsers.

- **Server-Side Rendering (SSR):** Implement SSR to improve website loading speeds and optimize performance while enhancing SEO capabilities.


## Running the Project

To run the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/dardangerguri/ft_transcendence ft_transcendence
   cd ft_transcendence
   ```

2. Launch the project using Docker:

   ```bash
   docker-compose up --build -d
   ```
3. Access the application:

   Once the containers are running, navigate to `https://localhost:8008` in your browser to access the application.

## Contributors

   - [Dardan Gërguri](https://github.com/dardangerguri)
   - [Joonas Henriksson](https://github.com/jnsh/)
   - [Aleksander Otsala](https://github.com/kenlies)
   - [Linus Broms](https://github.com/l-broms)
   - [Henriika Salmi](https://github.com/hcsalmi)
