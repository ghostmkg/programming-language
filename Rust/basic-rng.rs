use rand::Rng;
use std::io::{stdin, stdout, Write};
extern crate colored;
use colored::*;
use std::{thread, time};
#[allow(unused_macros)]
macro_rules! read {
    ($var:ident as $data_type:ty) => {
        let mut tmp = String::new();

        stdin().read_line(&mut tmp).expect("some prob hapend");

        let $var = tmp.trim().parse::<$data_type>().expect("some prob hapend");
    };
}
fn random(min: u64, max: u64) -> u64 {
    rand::thread_rng().gen_range(min..max)
}
fn main() {
    let mut count = 0;
    let mut stdout = stdout();
    let three_sec = time::Duration::from_secs(3);
    eprint!("enter minimum value: ");
    read!(a as u64);
    eprint!("enter maximum value: ");
    read!(b as u64);
    eprint!("enter the number u wanna find: ");
    read!(num as i128);
    loop {
        let number = random(a, b);
        print!("\r{} {}", "random number: ".red(), number);
        if i128::from(number) == num {
            print!("\r");
            println!(
                "\rThe number we waited for is here {:?} after {:?} times",
                number, count
            );
            thread::sleep(three_sec);
            break;
        } else {
            count += 1;
            stdout.flush().unwrap();
        }
    }
}
