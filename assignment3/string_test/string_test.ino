  char *wisdoms_idle[] = {
   "when it comes to meals there’s nothing quite like food",
   "there is a cool mushroom growing in the forest you could be looking at. instead you are in front of computer"
   "i love you",
   "you're pretty cool",
   "you should drop that class",
   "never trust a guy who doesn't like soup",
   "im hungry",
   "it looks like its going to rain",
   "i need a new catchphrase",
   "i want to go to the store to buy an onion",
   "i think i prefer oat milk over soy",
   "A grilled cheese consists of only these following items. Cheese. Bread with spread (usually butter). Add anything more and its called a 'melt'."
   };
   
   char *response_sound[] = {
   "what do you want?",
   "stop talking to me",
   "oh, tell me more."
   };

   char *response_touch[] = {
   "yes stroke me there",
   "i like that :)",
   "don't touch me that hard"
   };

   char *response_squeeze[] = {
    "did you wash your hands before touching me?",
    "i want you to hold my hand forever",
    "i feel loved :)"
   };


   int idle_count = *(&wisdoms_idle + 1) - wisdoms_idle;
   int resp_sound_count = *(&response_sound + 1) - response_sound;
   int resp_touch_count = *(&response_touch + 1) - response_touch;
   int resp_squeeze_count = *(&response_squeeze + 1) - response_squeeze;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
}

void loop() {
   long randNumber;
   randNumber = random(idle_count+1);
   Serial.println(wisdoms_idle[randNumber]);
   delay(2000);
  // put your main code here, to run repeatedly:
  
}
