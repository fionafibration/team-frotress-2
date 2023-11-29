"Resource/UI/SpectatorTournament.res"
{
	"specgui"
	{
		"ControlName"		"Frame"
		"fieldName"		"specgui"
		"wide"			"f0"
		"tall"			"480"
		"autoResize"	"0"
		"pinCorner"		"0"
		"enabled"		"1"
				
		"team1_player_base_offset_x"		"0"
		"team1_player_base_y"				"210"
		"team1_player_delta_x"				"0"
		"team1_player_delta_y"				"-19"
		"team2_player_base_offset_x"		"0"
		"team2_player_base_y"				"258"
		"team2_player_delta_x"				"0"
		"team2_player_delta_y"				"19"
		
		"playerpanels_kv"
		{
			"visible"		"0"
			"wide"			"121"
			"tall"			"17"
			"zpos"			"1"
			
			"color_ready"	"0 255 0 220"
			"color_notready"	"0 0 0 220"
			
			"PanelBG"
			{
				"ControlName"	"ImagePanel"
				"fieldName"		"PanelBG"
				"xpos"			"0"
				"ypos"			"0"
				"zpos"			"-1"
				"wide"			"128"
				"tall"			"18"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"enabled"		"1"
				"fillcolor"		"30 30 30 30"
			}
			
			"PanelCoverTop"
			{
				"ControlName"	"ImagePanel"
				"fieldName"		"PanelCoverTop"
				"xpos"			"0"
				"ypos"			"-1" // omp -- -1 for low-res grid.
				"zpos"			"3" // omp -- place above class image.
				"wide"			"128"
				"tall"			"4" // omp -- +1 for low-res grid.
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"0"
				"enabled"		"0"
				"fillcolor"		"30 30 30 255"
			}
			
			"PanelCoverBottom"
			{
				"ControlName"	"ImagePanel"
				"fieldName"		"PanelCoverBottom"
				"xpos"			"0"
				"ypos"			"15"
				"zpos"			"3" // omp -- place above class image.
				"wide"			"128"
				"tall"			"4" // omp -- +1 for low-res grid.
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"0"
				"enabled"		"0"
				"fillcolor"		"30 30 30 255"
			}
			
			"PanelCoverLeft"
			{
				"ControlName"	"ImagePanel"
				"fieldName"		"PanelCoverLeft"
				"xpos"			"15"
				"ypos"			"0"
				"zpos"			"-1"
				"wide"			"103"
				"tall"			"18"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"enabled"		"1"
				"fillcolor"		"30 30 30 255"
			}
			
			"PanelCoverLeft2"
			{
				"ControlName"	"ImagePanel"
				"fieldName"		"PanelCoverLeft2"
				"xpos"			"0"
				"ypos"			"0"
				"zpos"			"-1"
				"wide"			"18"
				"tall"			"18"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"enabled"		"1"
				"fillcolor"		"15 15 15 255"
			}
			
			"PanelCoverRight"
			{
				"ControlName"	"ImagePanel"
				"fieldName"		"PanelCoverRight"
				"xpos"			"125"
				"ypos"			"0"
				"zpos"			"-1"
				"wide"			"4" // omp -- +1 for low-res grid.
				"tall"			"18"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"0"
				"enabled"		"1"
				"fillcolor"		"30 30 30 255"
			}
			
			"playername"
			{
				"ControlName"	"CExLabel"
				"fieldName"		"playername"
				"font"			"Futura11"
				"xpos"			"20"
				"ypos"			"3"
				"zpos"			"5"
				"wide"			"55"
				"tall"			"12"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"labelText"		"%playername%"
				"textAlignment"	"west"
				"fgcolor"		"OmpText"
			}
			
			"classimage"
			{
				"ControlName"	"CTFClassImage"
				"fieldName"		"classimage"
				"xpos"			"1"
				"ypos"			"1"
				"zpos"			"2"
				"wide"			"16"
				"tall"			"16"
				"visible"		"1"
				"enabled"		"1"
				"image"			"../hud/class_scoutred"
				"scaleImage"	"1"	
				
				if_mvm
				{
					"image"			"../vgui/hud_connecting"
				}
			}
			
			"classimagebg"
			{
				"ControlName"		"Panel"
				"fieldName"		"classimagebg"
				"xpos"			"9999"
				"ypos"			"9999"
				"zpos"			"2"
				"wide"			"20"
				"tall"			"20"
				"visible"		"0"
				"enabled"		"1"
				"bgcolor_override"		"Black"
				"PaintBackgroundType"	"0"
			}
			
			"HealthIcon"
			{
				"ControlName"		"EditablePanel"
				"fieldName"			"HealthIcon"
				"xpos"				"0"
				"ypos"				"0"
				"zpos"				"3"
				"wide"				"24"
				"tall"				"18"
				"visible"			"1"
				"enabled"			"1"	
				"HealthBonusPosAdj"	"10"
				"HealthDeathWarning"		"0.49"
				"TFFont"					"HudFontSmallest"
				"HealthDeathWarningColor"	"HUDDeathWarning"
				"TextColor"					"HudOffWhite"
				"pin_to_sibling"	"PanelCoverLeft"
				"pin_corner_to_sibling" "PIN_TOPRIGHT"
				"pin_to_sibling_corner" "PIN_TOPRIGHT"
			}
			
			"ReadyBG"
			{
				"ControlName"		"ScalableImagePanel"
				"fieldName"		"ReadyBG"
				"xpos"			"30"
				"ypos"			"6"
				"zpos"			"-1"
				"wide"			"16"
				"tall"			"16"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"0"
				"enabled"		"1"
				"image"			"../HUD/tournament_panel_brown"

				"src_corner_height"	"22"				// pixels inside the image
				"src_corner_width"	"22"
			
				"draw_corner_width"	"3"				// screen size of the corners ( and sides ), proportional
				"draw_corner_height" 	"3"
				
				if_mvm
				{
					"visible"		"1"
				}	
			}
			
			"ReadyImage"
			{
				"ControlName"		"ImagePanel"
				"fieldName"		"ReadyImage"
				"xpos"			"32"
				"ypos"			"8"
				"zpos"			"0"
				"wide"			"12"
				"tall"			"12"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"0"
				"enabled"		"1"
				"image"			"hud/checkmark"
				"scaleImage"		"1"

				if_mvm
				{
					"visible"		"1"
				}
			}
			
			"respawntime"
			{
				"ControlName"	"CExLabel"
				"fieldName"		"respawntime"
				"font"			"Futura10"
				"xpos"			"94"
				"ypos"			"2"
				"zpos"			"5"
				"wide"			"24"
				"tall"			"14"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"labelText"		"%respawntime%"
				"textAlignment"	"center"
				"fgcolor"		"OmpRespawnTime"
			}

			"respawntimecover"
			{
				"ControlName"	"CExLabel"
				"fieldName"		"respawntimecover"
				"font"			"BlocksSharp64"
				"xpos"			"0"
				"ypos"			"0"
				"zpos"			"5"
				"wide"			"24"
				"tall"			"14"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"labelText"		"%respawntime%"
				"textAlignment"	"east"
				"fgcolor"		"30 30 30 255"
				"pin_to_sibling"	"PanelCoverLeft"
				"pin_corner_to_sibling" "PIN_TOPRIGHT"
				"pin_to_sibling_corner" "PIN_TOPRIGHT"
			}
			
			"chargeamount"
			{
				"ControlName"	"CExLabel"
				"fieldName"		"chargeamount"
				"font"			"Futura11"
				"xpos"			"71"
				"ypos"			"2"
				"zpos"			"6"
				"wide"			"22"
				"tall"			"14"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"labelText"		"%chargeamount%"
				"textAlignment"	"center"
				"fgcolor"		"OmpChargeAmount"
			}
			
			"specindex"
			{
				"ControlName"	"CExLabel"
				"fieldName"		"specindex"
				"font"			"DefaultVerySmall"
				"xpos"			"9999"
				"ypos"			"9999"
				"zpos"			"5"
				"wide"			"50"
				"tall"			"8"
				"autoResize"	"0"
				"pinCorner"		"0"
				"visible"		"1"
				"labelText"		"%specindex%"
				"textAlignment"	"north-west"
				//"fgcolor"		"235 226 202 255"
			}
		}
	}
	
	"MockupBar1"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"MockupBar1"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"-1"
		"wide"			"350"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"fillcolor"		"30 30 30 255"
	}
	"MockupBar2"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"MockupBar2"
		"xpos"			"c78"
		"ypos"			"0"
		"zpos"			"-1"
		"wide"			"350"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"fillcolor"		"30 30 30 255"
	}
	"MockupSideBar1"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"MockupSideBar1"
		"xpos"			"350"
		"ypos"			"0"
		"zpos"			"-1"
		"wide"			"3"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"image"			"../hud/color_panel_blu"
		
		"src_corner_height"		"23"
		"src_corner_width"		"23"
		"draw_corner_width"		"0"
		"draw_corner_height" 	"0"
	}
	"MockupSideBar2"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"MockupSideBar2"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"-1"
		"wide"			"3"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"image"			"../hud/color_panel_red"
		
		"src_corner_height"		"23"
		"src_corner_width"		"23"
		"draw_corner_width"		"0"
		"draw_corner_height" 	"0"
		
		"pin_to_sibling"	"MockupBar2"
		"pin_sibling_to_corner"	"PIN_TOPLEFT"
		"pin_corner_to_sibling"	"PIN_TOPRIGHT"
	}
	
	"MockupBluTeamLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"MockupBluTeamLabel"
		"font"			"Futura16"
		"fgcolor"		"OmpText"
		"labelText"		"creative juices"
		"textAlignment"		"east"
		"xpos"			"-30"
		"ypos"			"0"
		"wide"			"350"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
	}
	"MockupBluTeamScore"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"MockupBluTeamScore"
		"font"			"Futura24"
		"fgcolor"		"OmpText"
		"labelText"		"0"
		"textAlignment"		"east"
		"xpos"			"-4"
		"ypos"			"0"
		"wide"			"350"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
	}
	"MockupRedTeamLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"MockupRedTeamLabel"
		"font"			"Futura16"
		"fgcolor"		"OmpText"
		"labelText"		"Incredibly Mediocre"
		"textAlignment"		"west"
		"xpos"			"-32"
		"ypos"			"0"
		"wide"			"350"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		
		"pin_to_sibling" "MockupSideBar2"
		"pin_sibling_to_corner"	"PIN_TOPRIGHT"
		"pin_corner_to_sibling"	"PIN_TOPLEFT"
	}
	"MockupRedTeamScore"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"MockupRedTeamScore"
		"font"			"Futura24"
		"fgcolor"		"OmpText"
		"labelText"		"0"
		"textAlignment"		"west"
		"xpos"			"-6"
		"ypos"			"0"
		"wide"			"350"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		
		"pin_to_sibling" "MockupSideBar2"
		"pin_sibling_to_corner"	"PIN_TOPRIGHT"
		"pin_corner_to_sibling"	"PIN_TOPLEFT"
	}
	"topbar"
	{
		"ControlName"	"Panel"
		"fieldName"		"TopBar"
		"visible"		"0"
		"tall"			"0"
	}
	"BottomBar"
	{
		"ControlName"	"Frame"
		"fieldName"		"BottomBar"
		"visible"		"0"
		"ypos"			"100"
		"tall"			"0"
	}
	"bottombarblank"
	{
		"ControlName"		"Panel"
		"fieldName"		"bottombarblank"
		"visible"		"0"
		"ypos"			"480"
	}
	"ReinforcementsLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"ReinforcementsLabel"
		"xpos"			"c-300"
		"ypos"			"32"
		"wide"			"600"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#game_respawntime_in_secs"
		"textAlignment"		"center"
		"font"			"Futura16"
		"fgcolor"		"OmpText"
		
		if_mvm
		{
			"ypos"			"0"
		}
	}
	"BuyBackLabel"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"BuyBackLabel"
		"xpos"			"c-300"
		"ypos"			"87"
		"wide"			"600"
		"tall"			"14"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"#TF_PVE_Buyback"
		"textAlignment"	"center"
		"font"			"Futura12"
		"fgcolor"		"OmpText"
		"wrap"			"1"
		"centerwrap"	"1"
	
		if_mvm
		{
			"visible"		"1"
		}	
	}
	"MapLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"MapLabel"
		"visible"		"0"
	}
	"ClassOrTeamLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"ClassOrTeamLabel"
		"visible"		"0"
	}
	"SwitchCamModeKeyLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"SwitchCamModeKeyLabel"
		"visible"		"0"
		
	}
	"SwitchCamModeLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"SwitchCamModeLabel"
		"visible"		"0"
	}
	"CycleTargetFwdKeyLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"CycleTargetFwdKeyLabel"
		"visible"		"0"
	}
	"CycleTargetFwdLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"CycleTargetFwdLabel"
		"visible"		"0"
	}
	"CycleTargetRevKeyLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"CycleTargetRevKeyLabel"
		"visible"		"0"
	}
	"CycleTargetRevLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"CycleTargetRevLabel"
		"visible"		"0"
	}
	"TipLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"TipLabel"
		"visible"		"0"
	}
	"itempanel"
	{
		"ControlName"	"CItemModelPanel"
		"fieldName"		"itempanel"
		"xpos"			"r210"
		"ypos"			"c113"
		"zpos"			"1"
		"wide"			"140"
		"tall"			"100"
		"visible"		"0"
		"bgcolor_override"		"255 255 255 0"
		"PaintBackgroundType"	"0"
		"paintborder"	"0"
		
		"model_xpos"		"0"
		"model_center_x"    "1"
		"model_ypos"        "20"
		"model_wide"		"90"
		"model_tall"		"50"
		
		"text_xpos"		"0"
		"text_ypos"		"20"
		"text_wide"		"140"
		"text_center"	"1"
		
		"max_text_height"	"90"
		"padding_height"	"10"
		"resize_to_text"	"1"
		"text_forcesize"	"3"
		
		"ItemBG"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"ItemBG"
			"xpos"			"0"
			"ypos"			"0"
			"zpos"			"-1"
			"wide"			"200"
			"tall"			"1000"
			"autoResize"	"0"
			"pinCorner"		"0"
			"visible"		"1"
			"enabled"		"1"
			"fillcolor"		"OmpLightBG"
		}
		
		"itemmodelpanel"
		{
			"fieldName"		"itemmodelpanel"
			"use_item_rendertarget" "0"
			"useparentbg"		"1"
		}
		
		"ItemLabel"
		{	
			"ControlName"	"CExLabel"
			"fieldName"		"ItemLabel"
			"font"			"Futura9"
			"fgcolor"		"OmpText"
			"xpos"			"5"
			"ypos"			"5"
			"zpos"			"1"
			"wide"			"180"
			"tall"			"10"
			"autoResize"	"0"
			"pinCorner"		"0"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#FreezePanel_Item"
			"textAlignment"	"north-west"
			"dulltext"		"0"
			"brighttext"	"0"
		}
	}	
	
	"spectator_extras"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"spectator_extras"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"480"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
	}	
}
