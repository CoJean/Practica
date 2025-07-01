package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func binToHex(bin string) string {
	var hex string
	for i := 0; i < len(bin); i += 4 {
		group := bin[i:min(i+4, len(bin))]
		for len(group) < 4 {
			group += "0"
		}
		val := 0
		for j := 0; j < 4; j++ {
			if group[j] == '1' {
				val += 1 << (3 - j)
			}
		}
		hex += fmt.Sprintf("%X", val)
	}
	return hex
}

func hexToBin(hex string) string {
	var bin string
	for _, c := range hex {
		val := strings.TrimPrefix(fmt.Sprintf("%04b", hexCharToInt(byte(c))), " ")
		bin += val
	}
	return bin
}

func hexCharToInt(c byte) int {
	if c >= '0' && c <= '9' {
		return int(c - '0')
	}
	if c >= 'A' && c <= 'F' {
		return int(c - 'A' + 10)
	}
	return 0
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func convertFile(filename string) error {
	infile, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer infile.Close()

	var outputName string
	var convertLine func(string) string

	if strings.HasSuffix(filename, ".in") {
		outputName = filename + ".x"
		convertLine = func(line string) string {
			parts := strings.Split(line, ":")
			if len(parts) != 2 {
				return line
			}
			return parts[0] + ":" + binToHex(parts[1])
		}
	} else if strings.HasSuffix(filename, ".in.x") {
		outputName = strings.TrimSuffix(filename, ".x")
		convertLine = func(line string) string {
			parts := strings.Split(line, ":")
			if len(parts) != 2 {
				return line
			}
			return parts[0] + ":" + hexToBin(parts[1])
		}
	} else {
		return fmt.Errorf("Fișier necunoscut: %s", filename)
	}

	outfile, err := os.Create(outputName)
	if err != nil {
		return err
	}
	defer outfile.Close()

	scanner := bufio.NewScanner(infile)
	writer := bufio.NewWriter(outfile)

	for scanner.Scan() {
		line := scanner.Text()
		writer.WriteString(convertLine(line) + "\n")
	}

	writer.Flush()
	return nil
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: convert <filename>")
		return
	}
	filename := os.Args[1]
	err := convertFile(filename)
	if err != nil {
		fmt.Printf("Eroare: %v\n", err)
	}
}
