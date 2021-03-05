use tetra::graphics::{self, Color};
use tetra::{Context, ContextBuilder, State};

const SCREEN_WIDTH: i32 = 620;
const SCREEN_HEIGHT: i32 = 620;

struct GameState;

impl State for GameState {
    fn draw(&mut self, ctx: &mut Context) -> tetra::Result {
        graphics::clear(ctx, Color::WHITE);
        Ok(())
    }
}

fn main() -> tetra::Result {
    ContextBuilder::new("Tetris", SCREEN_WIDTH, SCREEN_HEIGHT)
        .build()?
        .run(|_| Ok(GameState))
}
