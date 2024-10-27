use std::io::{self, Write};
use std::process::Command;
use std::env;

fn main() {
    loop {
        print!("$ ");
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let input = input.trim();

        if input == "exit" {
            break;
        }

        let mut parts = input.split_whitespace();
        let command = parts.next().unwrap_or("");
        let args = parts.collect::<Vec<&str>>();

        match command {
            "cd" => {
                let new_dir = args.get(0).map_or("/", |s| *s);
                match env::set_current_dir(new_dir) {
                    Ok(_) => {},
                    Err(e) => eprintln!("Error changing directory: {}", e),
                }
            },
            "pwd" => {
                println!("{}", env::current_dir().unwrap().display());
            },
            "" => continue,
            _ => {
                let output = Command::new(command)
                    .args(&args)
                    .output();

                match output {
                    Ok(output) => {
                        io::stdout().write_all(&output.stdout).unwrap();
                        io::stderr().write_all(&output.stderr).unwrap();
                    },
                    Err(e) => eprintln!("Error executing command: {}", e),
                }
            }
        }
    }
}
