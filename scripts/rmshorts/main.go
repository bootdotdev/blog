package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
)

const contentPath = "content"

func main() {
	if len(os.Args) < 2 {
		log.Fatal("no code")
		return
	}

	code := os.Args[1]
	fmt.Println("removing shortcode:", code)

	err := filepath.Walk(contentPath,
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
			added := rmShort(string(dat), formattedShort(code))

			err = os.WriteFile(path, []byte(added), 0644)
			if err != nil {
				return err
			}
			return nil
		})
	if err != nil {
		log.Println(err)
	}
}

func formattedShort(short string) string {
	return fmt.Sprintf("{{< %s >}}", short)
}

func rmShort(in, shortcode string) (out string) {
	paras := strings.Split(in, "\n\n")
	newParas := []string{}
	for _, para := range paras {
		if para == shortcode {
			continue
		}
		newParas = append(newParas, para)
	}
	return strings.Join(newParas, "\n\n")
}
