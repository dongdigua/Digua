set nu
syntax on
set encoding=utf-8
call plug#begin('/home/digua/.vim/plugged')
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'altercation/vim-colors-solarized'
Plug 'mhartington/oceanic-next'
"Plug 'tomasr/molokai'
Plug 'joshdick/onedark.vim'
Plug 'JuliaEditorSupport/julia-vim'
call plug#end()
map tree :NERDTreeToggle
map '' :PlugInstall<CR>
"colorscheme OceanicNext
"let g:airline_theme='oceanicnext'
colorscheme onedark
let g:airline_theme='onedark'
set mouse=a
