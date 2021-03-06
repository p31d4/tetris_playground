#include <stdio.h>
#include <SDL2/SDL.h>

// Screen dimensions
const int SCREEN_WIDTH = 620;
const int SCREEN_HEIGHT = 620;

int main(int argc, char** argv)
{
    SDL_Window* window = NULL;
    SDL_Surface* screenSurface = NULL;

    if (0 > SDL_Init(SDL_INIT_VIDEO)) {

        printf("SDL initialization error: %s\n", SDL_GetError());
    }
    else {

        window = SDL_CreateWindow("Tetris", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
                                             SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
        if(NULL == window) {

            printf("Window initialization error: %s\n", SDL_GetError());
        }
	else {

            screenSurface = SDL_GetWindowSurface(window);

            SDL_FillRect(screenSurface, NULL, SDL_MapRGB(screenSurface->format, 0xFF, 0xFF, 0xFF));

            SDL_UpdateWindowSurface(window);

            bool run_tetris = true;
            SDL_Event event;

	    while(run_tetris) {
                while(SDL_PollEvent(&event)) {
                    if(event.type == SDL_QUIT)
                        run_tetris = false;
                }
            }
        }
    }

    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
