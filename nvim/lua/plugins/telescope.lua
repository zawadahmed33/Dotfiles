return {
	'nvim-telescope/telescope.nvim', tag = '0.1.8',
	dependencies = { 'nvim-lua/plenary.nvim' },
	config = function()
		require('telescope').setup{
			pickers = {
				find_files = {
					hidden = true
				}
			}	
		}
		local builtin = require("telescope.builtin")
		vim.keymap.set('n', '<leader>t', builtin.find_files, {})
	end
}
