" Disable windows bell sounds
set belloff=all

" Initialise vimplug
call plug#begin('~/.config/nvim/plugged')

Plug 'vim-airline/vim-airline'
Plug 'crusoexia/vim-monokai'

" Initialize plugin system
call plug#end()

" Enable syntax highlighting
syntax on

" Change colour scheme
colorscheme monokai

" Enable relative line numbers
set number relativenumber

" Disable background color of the theme
highlight Normal guibg=NONE ctermbg=NONE
highlight LineNr ctermbg=NONE
highlight CursorLineNr ctermbg=NONE

" Disable persistent search highlighting
set nohlsearch

" Set the spellcheck language to english
set spelllang=en

" Remap F6 to toggle spellcheck
nnoremap <silent> <F6> :set spell!<cr>
inoremap <silent> <F6> <C-O>:set spell!<cr>
