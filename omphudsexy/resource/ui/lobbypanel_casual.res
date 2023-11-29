#base "LobbyPanel.res"

"Resource/UI/LobbyPanel_Casual.res"
{
	"LobbyPanel"
	{
		"ControlName"	"Frame"
		"fieldName"		"LobbyPanel"
		"xpos"			"0"
		"ypos"			"50"
		"wide"			"f0"
		"tall"			"f0"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"tabPosition"	"0"
		"settitlebarvisible"	"0"
		"PaintBackgroundType"	"0"
		"bgcolor_override"	"46 43 42 0"
		"proportionaltoparent"	"1"
	}

	"ModeBackgroundImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"ModeBackgroundImage"
		"xpos"			"9999"
		"ypos"			"9999"
		"zpos"			"-1"
		"wide"			"f0"
		"tall"			"f0"
		"visible"		"0"
		"enabled"		"1"
		"mouseinputenabled" "0"
		"image"			"competitive/comp_background_tier001a"
		"scaleImage"	"1"
	}
	
	"CasualLabel"
	{
		"ControlName"	"Label"
		"fieldName"		"CasualLabel"
		"xpos"			"180"
		"ypos"			"0"
		"zpos"			"1"
		"wide"			"200"
		"tall"			"50"
		"labelText"		"casual"
		"font"			"Futura32"
		//"fgcolor_override"	"89 81 71 255"
		"fgcolor_override"	"255 255 255 255"
		"textAlignment"	"center"
		"sound_depressed"	"UI/buttonclick.wav"
		"sound_released"	"UI/buttonclickrelease.wav"
	}

	"GameModesContainer"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"GameModesContainer"
		"xpos"			"180"
		"ypos"			"r305"
		"zpos"			"100"
		"wide"			"200"
		"tall"			"190"
		"visible"		"1"
		"proportionaltoparent"	"1"

		"PlaylistBGPanel"
		{
			"ControlName"	"EditablePanel"
			"fieldName"		"PlaylistBGPanel"
			"xpos"			"cs-0.5"
			"ypos"			"0"
			"zpos"			"-1"
			"wide"			"p0.98"
			"tall"			"p1"
			"visible"		"1"
			"PaintBackgroundType"	"2"
			"border"		"NoBorder"
			"bgcolor_override"	"18 22 25 255"
			"proportionaltoparent"	"1"

			"pinCorner"		"2"
			"autoResize"	"1"
			

			"PlayListDropShadow"
			{
				"ControlName"	"EditablePanel"
				"fieldName"		"PlaylistBGPanel"
				"xpos"			"cs-0.5"
				"ypos"			"5"
				"zpos"			"100"
				"wide"			"p0.95"
				"tall"			"p0.95"
				"visible"		"1"
				"PaintBackgroundType"	"2"
				"border"		"InnerShadowBorder"
				"proportionaltoparent"	"1"
				"mouseinputenabled"	"0"
			}
			
			"Title"
			{
				"ControlName"		"Label"
				"fieldName"		"Title"
				"xpos"		"10"
				"ypos"		"5"
				"zpos"		"0"
				"wide"		"f0"
				"tall"		"20"
				"proportionaltoparent"	"1"
				"labeltext"		"#TF_Casual_MapSelection"
				"textAlignment"	"west"
				"font"			"HudFontMediumSmallBold"
		
				"mouseinputenabled"	"0"
			}

			"SelectedCount"
			{
				"ControlName"		"Label"
				"fieldName"		"SelectedCount"
				"xpos"		"10"
				"ypos"		"18"
				"zpos"		"0"
				"wide"		"f0"
				"tall"		"20"
				"proportionaltoparent"	"1"
				"labeltext"		"%selected_maps_count%"
				"textAlignment"	"west"
				"font"			"HudFontSmallest"
				"fgcolor_override"	"TanLight"
		
				"mouseinputenabled"	"1"
			}

			"QueueEstimation"
			{
				"ControlName"		"Label"
				"fieldName"		"QueueEstimation"
				"xpos"		"rs1-5"
				"ypos"		"18"
				"zpos"		"0"
				"wide"		"f0"
				"tall"		"20"
				"proportionaltoparent"	"1"
				"labeltext"		"#TF_Casual_QueueEstimation"
				"textAlignment"	"east"
				"font"			"HudFontSmallest"
				"fgcolor_override"	"TanLight"
				"textinsetx"	"5"
				"visible"	"0"
		
				"mouseinputenabled"	"0"
			}

			"GameModesList"
			{
				"ControlName"	"CScrollableList"
				"fieldName"		"GameModesList"
				"xpos"			"cs-0.5"
				"ypos"			"5"
				"wide"			"p0.95"
				"tall"			"p0.95"
				"visible"		"1"
				"proportionaltoparent"	"1"
				"restrict_width" "0"

				"bgcolor_override"	"0 0 0 255"

				"ScrollBar"
				{
					"ControlName"	"ScrollBar"
					"FieldName"		"ScrollBar"
					"xpos"			"rs1-1"
					"ypos"			"0"
					"tall"			"f0"
					"wide"			"5" // This gets slammed from client schme.  GG.
					"zpos"			"1000"
					"nobuttons"		"1"
					"proportionaltoparent"	"1"

					"Slider"
					{
						"fgcolor_override"	"TanDark"
					}
		
					"UpButton"
					{
						"ControlName"	"Button"
						"FieldName"		"UpButton"
						"visible"		"0"
					}
		
					"DownButton"
					{
						"ControlName"	"Button"
						"FieldName"		"DownButton"
						"visible"		"0"
					}
				}
			}
		}
	}


	"PartyActiveGroupBox"
	{
		"xpos"			"380"
		"ypos"		"r340"
		"tall"		"300"
		"proportionaltoparent"	"1"

		"PartyGroupBox"
		{
			"tall"		"160"
			"border"		"NoBorder"
			"bgcolor_override"	"18 22 25 225"
		}

		"ChatLog"
		{
			"ypos"			"165"
			"tall"			"100"
			"border"		"NoBorder"
			"bgcolor_override"	"18 22 25 225"
		}

		"ChatTextEntry"
		{
			"ypos"			"270"
			"tall"			"16"
			"border"		"NoBorder"
			"bgcolor_override"	"18 22 25 225"
		}
	}

	"SearchActiveGroupBox"
	{
		"xpos"		"180"
		"ypos"		"r305"
		"wide"		"190"
		"tall"		"190"
		"proportionaltoparent"	"1"
		"border"		"NoBorder"
		"bgcolor_override"	"18 22 25 225"

		"SearchActiveTitle"
		{
			"xpos"		"10"
			"ypos"		"5"
		}

		"NearbyColumnHead"
		{
			"font"			"Futura10"
			"xpos"		"rs1-90"
			"proportionaltoparent"	"1"
		}

		"WorldwideColumnHead"
		{
			"font"			"Futura10"
			"xpos"		"rs1-10"
			"proportionaltoparent"	"1"
		}

		"PlayersInGameLabel"
		{
			"font"			"Futura10Bold"
			"xpos"		"10"
		}

		"PlayersInGameTotalLabel"
		{
			"font"			"Futura10"
			"xpos"		"20"
			"ypos"		"85"
		}

			"PlayersInGameTotalNearbyValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-90"
				"ypos"		"85"
				"proportionaltoparent"	"1"
			}

			"PlayersInGameTotalWorldwideValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-10"
				"ypos"		"85"
				"proportionaltoparent"	"1"
			}

		"PlayersInGameMatchingLabel"
		{
			"font"			"Futura10"
			"xpos"		"20"
			"ypos"		"97"
		}

			"PlayersInGameMatchingNearbyValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-90"
				"ypos"		"97"
				"proportionaltoparent"	"1"
			}

			"PlayersInGameMatchingWorldwideValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-10"
				"ypos"		"97"
				"proportionaltoparent"	"1"
			}

		"PlayersSearchingLabel"
		{
			"font"			"Futura10Bold"
			"xpos"		"10"
			"ypos"		"120"
		}

		"PlayersSearchingTotalLabel"
		{
			"font"			"Futura10"
			"xpos"		"20"
			"ypos"		"135"
		}

			"PlayersSearchingTotalNearbyValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-90"
				"ypos"		"135"
				"proportionaltoparent"	"1"
			}

			"PlayersSearchingTotalWorldwideValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-10"
				"ypos"		"135"
				"proportionaltoparent"	"1"
			}

		"PlayersSearchingMatchingLabel"
		{
			"font"			"Futura10"
			"xpos"		"20"
			"ypos"		"147"
		}

			"PlayersSearchingMatchingNearbyValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-90"
				"ypos"		"147"
				"proportionaltoparent"	"1"
			}

			"PlayersSearchingMatchingWorldwideValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-10"
				"ypos"		"147"
				"proportionaltoparent"	"1"
			}

		"EmptyGameserversLabel"
		{
			"font"			"Futura10Bold"
			"xpos"		"10"
			"ypos"		"170"
		}

			"EmptyGameserversMatchingNearbyValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-90"
				"ypos"		"170"
				"proportionaltoparent"	"1"
			}

			"EmptyGameserversMatchingWorldwideValue"
			{
				"font"			"Futura10"
				"xpos"		"rs1-10"
				"ypos"		"170"
				"proportionaltoparent"	"1"
			}

		"PartyHasLowPriorityGroupBox"
		{
			"xpos"		"10"
			"ypos"		"rs1-10"
			"wide"		"f0"
			"tall"		"65"
			"proportionaltoparent"	"1"

			"PartyLowPriorityImage"
			{
				"xpos"			"0"
				"ypos"			"0"
				"wide"			"50"
				"tall"			"50"
				"scaleImage"	"1"
			}

			"PartyHasLowPriorityLabel"
			{
				"font"		"Futura10"
				"xpos"		"60"
				"ypos"		"0"
				"zpos"		"2"
				"wide"		"f70"
				"tall"		"f0"
				"textAlignment"	"north-west"
				"proportionaltoparent"	"1"
			}

			"PartyLowPriorityPenaltyTimer"
			{
				"font"		"Futura10"
				"xpos"		"60"
				"ypos"		"rs1"
				"wide"		"f0"
				"tall"		"30"
				"textAlignment"	"south-west"
				"proportionaltoparent"	"1"
			}
		}
	}
}
