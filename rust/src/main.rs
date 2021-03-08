use tetra::graphics::{self, Color, Rectangle};
use tetra::graphics::mesh::{GeometryBuilder, Mesh, ShapeStyle};
use tetra::{Context, ContextBuilder, State};
use tetra::math::Vec2;

const SCREEN_WIDTH: i32 = 620;
const SCREEN_HEIGHT: i32 = 620;
const GAME_SCREEN_WIDTH: f32 = 300.0;
const GAME_SCREEN_HEIGHT: f32 = 600.0;

struct GameState {
    mesh: Mesh,
}

impl GameState {
    fn new(ctx: &mut Context) -> tetra::Result<GameState> {

        let mesh = GeometryBuilder::new()
            .set_color(Color::BLACK)
            .rectangle (
                ShapeStyle::Fill,
                Rectangle::new(10.0, 10.0,
                    GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT),
            )?
            .set_color(Color::rgb(0.8, 0.6, 0.0))
            .rectangle (
                ShapeStyle::Stroke(10.0),
                Rectangle::new(0.0, 0.0,
                    SCREEN_WIDTH as f32, SCREEN_HEIGHT as f32),
            )?
            .build_mesh(ctx)?;

        Ok ( GameState {mesh} )
    }
}

impl State for GameState {
    fn draw(&mut self, ctx: &mut Context) -> tetra::Result {
        graphics::clear(ctx, Color::WHITE);

        self.mesh.draw(ctx, Vec2::new(0.0, 0.0));

        Ok(())
    }
}

fn main() -> tetra::Result {
    ContextBuilder::new("Tetris", SCREEN_WIDTH, SCREEN_HEIGHT)
        .quit_on_escape(true)
        .build()?
        .run(GameState::new)
}
