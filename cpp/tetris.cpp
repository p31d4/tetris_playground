#include <stdio.h>
#include <SDL2/SDL.h>
#include <string>
#include <cmath>

// Screen dimensions
const int SCREEN_WIDTH = 620;
const int SCREEN_HEIGHT = 620;

int main(int argc, char** argv) {

    SDL_Window* window = NULL;
    SDL_Renderer* renderer = NULL;
    bool infra_initialized = false;

    if(0 > SDL_Init(SDL_INIT_VIDEO)) {
        printf("SDL initilization error: %s\n", SDL_GetError());
    }
    else {

        if(!SDL_SetHint( SDL_HINT_RENDER_SCALE_QUALITY, "1")) {
            printf("Failed to enable linear texture filtering!");
        }

        window = SDL_CreateWindow("Tetris", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
                                             SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
        if(NULL == window) {
            printf("Window initialization error: %s\n", SDL_GetError());
        }
        else {
            renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
            if(NULL == renderer) {
                printf("Renderer initilization error: %s\n", SDL_GetError());
            }
            else {
                SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF);
		infra_initialized = true;
            }
        }
    }

    if(infra_initialized) {

        bool run_tetris = true;
        SDL_Event event;

        while(run_tetris) {

            while(0 != SDL_PollEvent(&event)) {
                if(event.type == SDL_QUIT) {
                    run_tetris = false;
                }
            }

            // Clear screen
            SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF);
            SDL_RenderClear(renderer);

            // Render Tetris screen
            SDL_Rect fillRect = {10, 10, SCREEN_WIDTH - 320, SCREEN_HEIGHT - 20};
            SDL_SetRenderDrawColor(renderer, 0x00, 0x00, 0x00, 0xFF);
            SDL_RenderFillRect(renderer, &fillRect);

            // I took the "dirty hack" way as it looks like SDL2 does not
            // support increasing the thickness and this is a Proof of Concept
            // Maybe I go through the SDL_glx library in the future and check
            // how people there solved the problem
            SDL_SetRenderDrawColor(renderer, 0xCC, 0x99, 0x00, 0xFF);
            SDL_Rect border_rect;
            for (uint8_t counter = 0; counter < 5; counter += 1) {
                border_rect.x = counter;
                border_rect.y = counter;
                border_rect.w = SCREEN_WIDTH - counter * 2;
                border_rect.h = SCREEN_HEIGHT - counter * 2;
                SDL_RenderDrawRect(renderer, &border_rect);
            }

            // Update Tetris screen
            SDL_RenderPresent(renderer);
        }
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    window = NULL;
    renderer = NULL;

    SDL_Quit();

    return 0;
}
