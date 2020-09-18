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
Plug 'vim-airline/vim-airline'
Plug 'crusoexia/vim-monokai'
call plug#end()


" Enable syntax highlighting
syntax on
" Set the spellcheck language to english
set spelllang=en

" Change colour scheme
colorscheme monokai


" Disable background color of the theme
highlight Normal guibg=NONE ctermbg=NONE
highlight LineNr ctermbg=NONE
highlight CursorLineNr ctermbg=NONE



" Remap F6 to toggle spellcheck
nnoremap <silent> <F6> :set spell!<cr>
inoremap <silent> <F6> <C-O>:set spell!<cr>
