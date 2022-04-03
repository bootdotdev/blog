package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

const contentPath = "content"

func main() {
	if len(os.Args) < 2 {
		log.Fatal("no code")
		return
	}
	if len(os.Args) < 3 {
		log.Fatal("no section number")
		return
	}

	code := os.Args[1]

	sectionNum, err := strconv.Atoi(os.Args[2])
	if err != nil {
		log.Fatalf("section number: %v", err)
	}

	fmt.Println("adding shortcode:", code, "at end of section:", sectionNum)

	count := 0

	err = filepath.Walk(contentPath,
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			if info.IsDir() {
				return nil
			}

			// we only want posts, not pages
			parts := strings.Split(path, "/")
			if len(parts) < 3 {
				return nil
			}

			dat, err := os.ReadFile(path)
			if err != nil {
				return err
			}
			out, added := addShort(string(dat), formattedShort(code), sectionNum)
			if added {
				count++
			}

			err = os.WriteFile(path, []byte(out), 0644)
			if err != nil {
				return err
			}
			return nil
		})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("added", count, "shortcodes")
}

func formattedShort(short string) string {
	return fmt.Sprintf("{{< %s >}}", short)
}

func addShort(in, shortcode string, sectionNum int) (out string, added bool) {
	paras := strings.Split(in, "\n\n")
	newParas := []string{}

	currentSection := 1

	inCodeBlock := false

	for i, para := range paras {
		newParas = append(newParas, para)

		if isHeadline(para) {
			currentSection++
		}
		if isGuard(para) {
			inCodeBlock = !inCodeBlock
		}

		// only add it once
		if added {
			continue
		}

		if inCodeBlock {
			continue
		}

		// don't place until the end of the section number provided
		if currentSection < sectionNum {
			continue
		}
		if i+1 >= len(paras) {
			continue
		}
		if !isHeadline(paras[i+1]) {
			continue
		}

		newParas = append(newParas, shortcode)
		added = true
	}
	return strings.Join(newParas, "\n\n"), added
}

func isHeadline(in string) bool {
	return strings.HasPrefix(in, "## ")
}

func isGuard(in string) bool {
	return strings.HasPrefix(in, "```")
}
