# convert
pandoc -f docx -t gfm --wrap=none -o out.md $1

# remove stupid underlines
sed -i '.bak' 's/<u>//g' "out.md"
sed -i '.bak' 's/<\/u>//g' "out.md"

# remove smart quotes
sed -i '.bak' 's/“/"/g' "out.md"
sed -i '.bak' 's/”/"/g' "out.md"

# Fix bullet points
sed -i '.bak' 's/- /* /g' "out.md"

# Fix absolute links
sed -i '.bak' 's/(https:\/\/blog.boot.dev/(/g' "out.md"

# no h1s in the article
sed -i '.bak' 's/^# /## /g' "out.md"

rm out.md.bak
