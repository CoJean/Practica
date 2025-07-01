use std::env;
use std::fs::{self, File};
use std::io::{BufRead, BufReader, BufWriter, Write};
use std::path::Path;


fn main() {
    let args: Vec<String> = env::args().collect();
    let mut cache_size = 0;

    if args.contains(&"--cache-size".to_string()) {
        if let Some(pos) = args.iter().position(|x| x == "--cache-size") {
            if let Some(size_str) = args.get(pos + 1) {
                cache_size = size_str.parse().unwrap_or(0);
            }
        }
    }
    
fn bin_to_hex(bin: &str) -> String {
    bin.as_bytes()
        .chunks(4)
        .map(|chunk| {
            let s = std::str::from_utf8(chunk).unwrap();
            let val = u8::from_str_radix(s, 2).unwrap();
            format!("{:X}", val)
        })
        .collect()
}

fn hex_to_bin(hex: &str) -> String {
    hex.chars()
        .map(|c| {
            let val = u8::from_str_radix(&c.to_string(), 16).unwrap();
            format!("{:04b}", val)
        })
        .collect()
}

fn convert_to_hex(input_file: &str) {
    let reader = BufReader::new(File::open(input_file).expect("Cannot open input file"));
    let output_file = format!("{}.x", input_file);
    let mut writer = BufWriter::new(File::create(&output_file).expect("Cannot create output file"));

    for line in reader.lines() {
        let line = line.unwrap();
        if let Some((dims, data)) = line.split_once(':') {
            let hex = bin_to_hex(data);
            writeln!(writer, "{}:{}", dims, hex).unwrap();
        }
    }

    println!("Converted to HEX: {}", output_file);
}

fn convert_to_bin(input_file: &str) {
    let reader = BufReader::new(File::open(input_file).expect("Cannot open input file"));
    let output_file = input_file.strip_suffix(".x").unwrap_or("mat.out");
    let mut writer = BufWriter::new(File::create(output_file).expect("Cannot create output file"));

    for line in reader.lines() {
        let line = line.unwrap();
        if let Some((dims, data)) = line.split_once(':') {
            let bin = hex_to_bin(data);
            writeln!(writer, "{}:{}", dims, bin).unwrap();
        }
    }

    println!("Converted to BIN: {}", output_file);
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: convert <input_file>");
        return;
    }

    let input_file = &args[1];

    if input_file.ends_with(".in.x") {
        convert_to_bin(input_file);
    } else if input_file.ends_with(".in") {
        convert_to_hex(input_file);
    } else {
        eprintln!("Unknown file type. Use .in or .in.x files.");
    }
}
