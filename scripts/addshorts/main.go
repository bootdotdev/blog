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
		log.Fatal("no para number")
		return
	}

	code := os.Args[1]

	paraNum, err := strconv.Atoi(os.Args[2])
	if err != nil {
		log.Fatalf("para num: %v", err)
	}

	fmt.Println("adding shortcode:", code, "at paragraph: %v", paraNum)

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
			added := addShort(string(dat), formattedShort(code), paraNum)

			err = os.WriteFile(path, []byte(added), 0644)
			if err != nil {
				return err
			}
			os.Exit(1)
			return nil
		})
	if err != nil {
		log.Println(err)
	}
}

func formattedShort(short string) string {
	return fmt.Sprintf("{{< %s >}}", short)
}

func addShort(in, shortcode string, numParas int) (out string) {
	paras := strings.Split(in, "\n\n")
	newParas := []string{}
	added := false
	for i, para := range paras {
		newParas = append(newParas, para)

		if added {
			continue
		}
		if i < numParas {
			continue
		}
		if i == 0 {
			continue
		}
		if isHeadline(paras[i-1]) {
			continue
		}
		if i == len(paras)-1 {
			continue
		}
		newParas = append(newParas, shortcode)
		added = true
	}
	return strings.Join(newParas, "\n\n")
}

func isHeadline(in string) bool {
	return strings.HasPrefix(in, "#")
}
