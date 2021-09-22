//A simple video player made by Kaloyan Kolev for CPSC334
//Select your video file by uncommenting below and press the Play button on top

import processing.video.*;

// Declare a Movie object.
Movie movie;

// Pick which video you want to play - uncomment the option you want 
String movieName = "lake.mp4";
//String movieName = "sunset.mp4";
//String movieName = "clouds.mp4";
//String movieName = "beach.mp4";

void setup() {
  fullScreen(0);

  // Initialize Movie object. The file should live in the data folder.
  movie = new Movie(this, movieName);

  // Start playing movie. Loop() is broken for large video files, so we use function below to loop manually.
  movie.loop();
}

// Read new frames from the movie.
void movieEvent(Movie movie) {
  movie.read();
}

//Check if movie is done
boolean is_movie_finished(Movie m) {
  return m.duration() - m.time() < 0.05;
}

// Display movie.
void draw() {
  
  image(movie, 1024, 0); //Offset by 1024px so it doesn't display on the small monitor
  if (is_movie_finished(movie)){
    movie.jump(0); //Replay
  };
}
