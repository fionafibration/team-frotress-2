"Resource/UI/LobbyLeaderboard.res"
{
	"BookPage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"BookPage"
		"xpos"			"s-0.1667"
		"ypos"			"0"
		"zpos"			"0"
		"wide"			"o1"
		"tall"			"f0"
		"visible"		"0"
		"enabled"		"1"
		"image"			""
		"scaleImage"	"1"
		"proportionaltoparent" "1"
	}
	
		"LocalLeaderboardButton"
	{
		"ControlName"	"CExButton"
		"fieldName"		"LocalLeaderboardButton"
		"xpos"			"p0.05"
		"ypos"			"2"
		"zpos"			"0"
		"wide"			"p0.44"
		"tall"			"15"
		"visible"		"1"
		"proportionaltoparent"	"1"
		
		"defaultFgColor_override" "TanLight"
		"armedFgColor_override" "TanLight"
		"depressedFgColor_override" "TanLight"
		"defaultBgColor_override" "13 17 20 255"
		"armedBgColor_override"	  "33 37 40 255"
		"depressedBgColor_override"	"33 37 40 255"
		"border_default"	"NoBorder"
		
		"actionsignallevel"		"1"
		"command"		"local"
		"labeltext"		"Friends"
		"font"			"HudFontSmallestBold"
		"fgcolor_override"	"TanLight"
		"textAlignment"	"center"

		"sound_depressed"	"UI/buttonclick.wav"
		"sound_released"	"UI/buttonclickrelease.wav"
	}

	"GlobalLeaderboardButton"
	{
		"ControlName"	"CExButton"
		"fieldName"		"GlobalLeaderboardButton"
		"xpos"			"rs1-p0.05"
		"ypos"			"2"
		"zpos"			"0"
		"wide"			"p0.44"
		"tall"			"15"
		"visible"		"1"
		"proportionaltoparent"	"1"
		
		"defaultFgColor_override" "TanLight"
		"armedFgColor_override" "TanLight"
		"depressedFgColor_override" "TanLight"
		"defaultBgColor_override" "13 17 20 255"
		"armedBgColor_override"	  "33 37 40 255"
		"depressedBgColor_override"	"33 37 40 255"
		"border_default"	"NoBorder"

		"actionsignallevel"		"1"
		"command"		"global"
		"labeltext"		"Global"
		"font"			"HudFontSmallestBold"
		"fgcolor_override"	"TanLight"
		"textAlignment"	"center"

		"sound_depressed"	"UI/buttonclick.wav"
		"sound_released"	"UI/buttonclickrelease.wav"
	}


	"Line"
	{
		"ControlName"		"EditablePanel"
		"fieldName"			"Line"
		"xpos"				"0"
		"ypos"				"20"
		"wide"				"240"
		"tall"				"2"
		"visible"			"1"
		"proportionaltoparent" "1"

		"bgcolor_override"	"OmpHighlights"
	}

	"ScoreListScroller"
	{
		"ControlName"		"ScrollableEditablePanel"
		"fieldName"			"ScoreListScroller"
		"xpos"				"-10"
		"ypos"				"30"
		"wide"				"205"
		"tall"				"220"
		"visible"			"1"
		"proportionaltoparent" "1"
		"asynchandling"		"hide"
	}

	"LoadingImage"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"LoadingImage"
		"xpos"				"cs-0.5"
		"ypos"				"cs-0.5"
		"zpos"				"1"
		"wide"				"p0.75"
		"tall"				"w1"
		"visible"			"1"
		"enabled"			"1"
		"image"				"animated/tf2_logo_hourglass"
		"scaleImage"		"1"
		"proportionaltoparent" "1"
		"asynchandling"		"show"
	}
}
