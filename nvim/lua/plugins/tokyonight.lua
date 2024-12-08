return {
	{
		"folke/tokyonight.nvim",
		lazy = false,
		priority = 1000,
		opts = {
			transparent = true
		},
		config = function()
			vim.cmd.colorscheme("tokyonight-moon")
		end
	}
}
