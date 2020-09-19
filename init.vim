" Enable standard and relative line numbers
set number
set relativenumber
" Preserves buffers when switching them
set hidden
" Disable all bells
set belloff=all
" Use tabs of equivalent 4 spaces for display
set autoindent noexpandtab tabstop=4 shiftwidth=4
" Disable mode display, made unnecessary with airline
set noshowmode
" Keep the cursor from scrolling to the top and bottom
set scrolloff=8
" Enable the mouse
set mouse=a


" Disable persistent search highlighting
" TODO - Plugin can do this better I think
" set ignorecase
" set smartcase
set nohlsearch
set incsearch
" TODO
" set termguicolors
" set completeopt=menuone,noinsert,noselect


" Initialise vimplug
call plug#begin('~/.config/nvim/plugged')
" Colour scheme
Plug 'crusoexia/vim-monokai'
Plug 'vim-airline/vim-airline'
Plug 'tpope/vim-commentary'

Plug 'vim-airline/vim-airline-themes'

call plug#end()

" Enable syntax highlighting
syntax on
" Set the spell check language to English
set spelllang=en_au

" Change colour scheme
colorscheme monokai
let g:airline_theme="badwolf"


" Disable background colour of the theme
highlight Normal guibg=NONE ctermbg=NONE
highlight LineNr ctermbg=NONE
highlight CursorLineNr ctermbg=NONE


" Remove trailing whitespace on save
autocmd BufWritePre * %s/\s\+$//e

" Keep visual block highlighted after indent
vnoremap < <gv
vnoremap > >gv

" Remap F6 to toggle spellcheck
nnoremap <silent> <F6> :set spell!<cr>
inoremap <silent> <F6> <C-O>:set spell!<cr>
