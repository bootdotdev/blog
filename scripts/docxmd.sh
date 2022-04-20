# convert
pandoc -f docx -t markdown_strict --wrap=none -o out.md $1

# remove stupid underlines
sed -i '.bak' 's/<u>//g' "out.md"
sed -i '.bak' 's/<\/u>//g' "out.md"

# no h1s in the article
sed -i '.bak' 's/^# /## /g' "out.md"

rm out.md.bak
