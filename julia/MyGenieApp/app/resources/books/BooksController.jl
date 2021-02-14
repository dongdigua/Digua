module BooksController
function billgatesbooks()
  html(:books, "billbooks.jl.md", books = BillGatesBooks)
end
end
