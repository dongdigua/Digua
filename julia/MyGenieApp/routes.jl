using Genie.Router
using BooksController

route("/bgbooks", BooksController.billbooks)

route("/") do
  serve_static_file("welcome.html")
end

route("/hello") do
	"hello"
end
