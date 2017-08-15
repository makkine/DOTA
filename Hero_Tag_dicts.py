#---------------------------------------------------------------------- 
# hero_dict is a dictionary whose keys are hero_id_tags and whose 
# values are in-game category tags describing attributes of heroes
# 
# tags '1','2','3' = indicators difficulty of play 
# tags 'female', 'male', 'neuter' = presented gender of hero
# tags 'agi', 'int', 'str' = main attribute hero uses 
# the other tags mark in-gagme categories of relevence 
# 
# except for difficulty level and gender and main attribute, tags are not (usually) mutually  
# exclusive and are not used uniformly or exuaustively across heroes
#---------------------------------------------------------------------- 


# h_tags is a list of tags
h_tags = ['1', '2', '3', 
          'female', 'male', 'neuter',
          'agi', 'int', 'str',
          'carry', 'disabler', 'durable', 'escape', 'initiator',  
          'jungler',  'melee',  'nuker', 'pusher', 'ranged', 'support', 
          'rattletrap', 'furion', 'obsidian_destroyer', 'wisp',  'nevermore', 'shredder', 'necrolyte', 'magnataur', 'winter_wyvern', 'mirana', 'batrider', 'windrunner', 'oracle', 'sven', 'shadow_demon', 'vengefulspirit', 'skywrath_mage', 'skeleton_king', 'naga_siren', 'doom_bringer', 'treant', 'venomancer', 'abyssal_underlord', 'io', 'ursa', 'huskar', 'bounty_hunter', 'elder_titan', 'templar_assassin', 'death_prophet', 'drow_ranger', 'outworld devourer', 'pugna', 'lycan', 'life_stealer', 'morphling', 'monkey_king', 'leshrac', 'antimage', 'enigma', 'medusa', 'razor', 'tiny', 'chen', 'bloodseeker', 'undying', 'shadow_shaman', 'bane', 'lone_druid', 'centaur', 'keeper_of_the_light', 'enchantress', 'rubick', 'phantom_lancer', 'tinker', 'sniper', 'lich', 'puck', 'invoker', 'dark_seer', 'lion', 'kunkka', 'arc_warden', 'nyx_assassin', 'broodmother', 'viper', 'luna', 'meepo', 'axe', 'earthshaker', 'techies', 'juggernaut', 'visage', 'ancient_apparition', 'chaos_knight', 'spirit_breaker', 'beastmaster', 'legion_commander', 'abaddon', 'jakiro', 'ember_spirit', 'alchemist', 'pudge', 'omniknight', 'terrorblade', 'slark', 'warlock', 'storm_spirit', 'troll_warlord', 'clinkz', 'night_stalker', 'slardar', 'queenofpain', 'zuus', 'dazzle', 'dragon_knight', 'phantom_assassin', 'riki', 'tusk', 'spectre', 'bristleback', 'tidehunter', 'witch_doctor', 'sand_king', 'lina', 'phoenix', 'weaver', 'gyrocopter', 'crystal_maiden', 'brewmaster', 'silencer', 'earth_spirit', 'disruptor', 'faceless_void', 'ogre_magi']

difficulty_tags = ['1', '2', '3']
gender_tags = ['female', 'male', 'neuter']
skill_tags = ['agi', 'int', 'str']


hero_dict = {}
hero_dict['npc_dota_hero_antimage'] = ['antimage','male', 'melee', 'agi', 'carry', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_axe'] = ['axe','male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'jungler', '1']
hero_dict['npc_dota_hero_bane'] = ['bane','male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'durable', '2']
hero_dict['npc_dota_hero_bloodseeker'] = ['bloodseeker','male', 'melee', 'agi', 'carry', 'disabler', 'nuker', 'jungler', 'initiator', '1']
hero_dict['npc_dota_hero_crystal_maiden'] = ['crystal_maiden', 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '1']
hero_dict['npc_dota_hero_drow_ranger'] = ['drow_ranger', 'female', 'ranged', 'agi', 'carry', 'disabler', 'pusher', '1']
hero_dict['npc_dota_hero_earthshaker'] = ['earthshaker','male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_juggernaut'] = ['juggernaut', 'male', 'melee', 'agi', 'carry', 'pusher', 'escape', '1']
hero_dict['npc_dota_hero_mirana'] = ['mirana', 'female', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'support', 'disabler', '2']
hero_dict['npc_dota_hero_nevermore'] = ['nevermore', 'male', 'ranged', 'agi', 'carry', 'nuker', '2']
hero_dict['npc_dota_hero_morphling'] = ['morphling','male', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'durable', 'disabler', '3']
hero_dict['npc_dota_hero_phantom_lancer'] = ['phantom_lancer', 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_puck'] = ['puck','female', 'ranged', 'int', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_pudge'] = ['pudge', 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_razor'] = ['razor','male', 'ranged', 'agi', 'carry', 'durable', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_sand_king'] = ['sand_king', 'male', 'melee', 'str', 'initiator', 'escape', 'disabler', 'nuker', 'jungler', '2']
hero_dict['npc_dota_hero_storm_spirit'] = ['storm_spirit','male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'initiator', 'escape', '3']
hero_dict['npc_dota_hero_sven'] = ['sven', 'male', 'melee', 'str', 'carry', 'durable', 'disabler', 'initiator', 'nuker', '1']
hero_dict['npc_dota_hero_tiny'] = ['tiny', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'pusher', 'durable']
hero_dict['npc_dota_hero_vengefulspirit'] = ['vengefulspirit', 'female', 'ranged', 'agi', 'support', 'escape', 'nuker', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_windrunner'] = ['windrunner', 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_zuus'] = ['zuus', 'male', 'ranged', 'int', 'nuker', '1']
hero_dict['npc_dota_hero_kunkka'] = ['kunkka','male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_lina'] = ['lina', 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', '1']
hero_dict['npc_dota_hero_lich'] = ['lich', 'male', 'ranged', 'int', 'support', 'nuker', '1']
hero_dict['npc_dota_hero_lion'] = ['lion', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '1']
hero_dict['npc_dota_hero_shadow_shaman'] = ['shadow_shaman', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'initiator', '1']
hero_dict['npc_dota_hero_slardar'] = ['slardar', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_tidehunter'] = ['tidehunter', 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_witch_doctor'] = ['witch_doctor', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_riki'] = ['riki', 'male', 'melee', 'agi', 'carry', 'escape', 'disabler', '1']
hero_dict['npc_dota_hero_enigma'] = ['enigma', 'male', 'ranged', 'int', 'pusher', 'disabler', 'initiator', 'jungler', '2']
hero_dict['npc_dota_hero_tinker'] = ['tinker', 'male', 'ranged', 'int', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_sniper'] = ['sniper', 'male', 'ranged', 'agi', 'carry', 'nuker', '1']
hero_dict['npc_dota_hero_necrolyte'] = ['necrolyte', 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_warlock'] = ['warlock', 'male', 'ranged', 'int', 'support', 'disabler', 'initiator', '1']
hero_dict['npc_dota_hero_beastmaster'] = ['beastmaster', 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_queenofpain'] = ['queenofpain', 'female', 'ranged', 'int', 'carry', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_venomancer'] = ['venomancer', 'male', 'ranged', 'agi', 'support', 'initiator', 'nuker', 'pusher', 'disabler', '1']
hero_dict['npc_dota_hero_faceless_void'] = ['faceless_void', 'male', 'melee', 'agi', 'carry', 'escape', 'initiator', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_skeleton_king'] = ['skeleton_king', 'male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'carry']
hero_dict['npc_dota_hero_death_prophet'] = ['death_prophet', 'female', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_phantom_assassin'] = ['phantom_assassin', 'female', 'melee', 'agi', 'carry', 'escape', '1']
hero_dict['npc_dota_hero_pugna'] = ['pugna', 'male', 'ranged', 'int', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_templar_assassin'] = ['templar_assassin', 'female', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_viper'] = ['viper', 'male', 'ranged', 'agi', 'carry', 'durable', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_luna'] = ['luna', 'female', 'ranged', 'agi', 'carry', 'pusher', 'nuker', '1']
hero_dict['npc_dota_hero_dragon_knight'] = ['dragon_knight', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable', 'pusher']
hero_dict['npc_dota_hero_dazzle'] = ['dazzle', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_rattletrap'] = ['rattletrap', 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_leshrac'] = ['leshrac', 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'support', 'pusher', '1']
hero_dict['npc_dota_hero_furion'] = ['furion', 'male', 'ranged', 'int', 'carry', 'escape', 'nuker', 'jungler', 'pusher', '2']
hero_dict['npc_dota_hero_life_stealer'] = ['life_stealer', 'male', 'melee', 'str', 'durable', 'jungler', 'disabler', 'carry', 'escape']
hero_dict['npc_dota_hero_dark_seer'] = ['dark_seer', 'male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_clinkz'] = ['clinkz', 'male', 'ranged', 'agi', 'carry', 'escape', 'pusher', '2']
hero_dict['npc_dota_hero_omniknight'] = ['omniknight', 'male', 'melee', 'str', 'durable', 'support', 'nuker']
hero_dict['npc_dota_hero_enchantress'] = ['enchantress','female', 'ranged', 'int', 'support', 'disabler', 'pusher', 'jungler', 'durable', '2']
hero_dict['npc_dota_hero_huskar'] = ['huskar', 'male', 'ranged', 'str', 'initiator', 'carry', 'durable']
hero_dict['npc_dota_hero_night_stalker'] = ['night_stalker', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_broodmother'] = ['broodmother', 'female', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_bounty_hunter'] = ['bounty_hunter', 'male', 'melee', 'agi', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_weaver'] = ['weaver', 'male', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_jakiro'] = ['jakiro', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_batrider'] = ['batrider', 'male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_chen'] = ['chen', 'male', 'ranged', 'int', 'support', 'pusher', 'jungler', '3']
hero_dict['npc_dota_hero_spectre'] = ['spectre', 'female', 'melee', 'agi', 'carry', 'escape', 'durable', '2']
hero_dict['npc_dota_hero_doom_bringer'] = ['doom_bringer', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_ancient_apparition'] = ['ancient_apparition', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ursa'] = ['ursa','male', 'melee', 'agi', 'carry', 'jungler', 'durable', 'disabler', '1']
hero_dict['npc_dota_hero_spirit_breaker'] = ['spirit_breaker', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_gyrocopter'] = ['gyrocopter', 'male', 'ranged', 'agi', 'carry', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_alchemist'] = ['alchemist', 'male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker', 'carry', 'durable']
hero_dict['npc_dota_hero_invoker'] = ['invoker', 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'escape', 'pusher', '3']
hero_dict['npc_dota_hero_silencer'] = ['silencer', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'initiator', '2']
hero_dict['npc_dota_hero_obsidian_destroyer'] = ['obsidian_destroyer', 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_lycan'] = ['lycan', 'male', 'melee', 'str', 'carry', 'pusher', 'jungler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_brewmaster'] = ['brewmaster', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_shadow_demon'] = ['shadow_demon', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_lone_druid'] = ['lone_druid', 'male', 'ranged', 'agi', 'carry', 'pusher', 'jungler', 'durable', '3']
hero_dict['npc_dota_hero_meepo'] = ['meepo', 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', 'pusher', '3']
hero_dict['npc_dota_hero_keeper_of_the_light'] = ['keeper_of_the_light', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '2']
hero_dict['npc_dota_hero_visage'] = ['visage', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'durable', '3']
hero_dict['npc_dota_hero_disruptor'] = ['disruptor', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_rubick'] = ['rubick', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '3']
hero_dict['npc_dota_hero_ogre_magi'] = ['ogre_magi', 'male', 'melee', 'int', 'support', 'disabler', 'nuker', 'durable', 'initiator', '1']
hero_dict['npc_dota_hero_nyx_assassin'] = ['nyx_assassin', 'male', 'melee', 'agi', 'disabler', 'initiator', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_naga_siren'] = ['naga_siren', 'female', 'melee', 'agi', 'carry', 'escape', 'support', 'pusher', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_undying'] = ['undying', 'male', 'melee', 'str', 'nuker', 'support', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_chaos_knight'] = ['chaos_knight', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'pusher', '1']
hero_dict['npc_dota_hero_wisp'] = ['wisp', 'neuter', 'ranged', 'str', 'escape', 'support', 'nuker', '3']
hero_dict['npc_dota_hero_treant'] = ['treant', 'male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_magnataur'] = ['magnataur', 'male', 'melee', 'str', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_centaur'] = ['centaur', 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '1']
hero_dict['npc_dota_hero_slark'] = ['slark', 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', '1']
hero_dict['npc_dota_hero_shredder'] = ['shredder','male', 'melee', 'str', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_medusa'] = ['medusa', 'female', 'ranged', 'agi', 'carry', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_troll_warlord'] = ['troll_warlord', 'male', 'ranged', 'agi', 'carry', 'pusher', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_techies'] = ['techies', 'male', 'ranged', 'int', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_abaddon'] = ['abaddon', 'male', 'melee', 'str', 'carry', 'support', 'durable', '1']
hero_dict['npc_dota_hero_bristleback'] = ['bristleback', 'male', 'melee', 'str', 'initiator', 'carry', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_abyssal_underlord'] = ['abyssal_underlord', 'male', 'melee', 'str', 'support', 'disabler', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_legion_commander'] = ['legion_commander', 'female', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'nuker', '1']
hero_dict['npc_dota_hero_earth_spirit'] = ['earth_spirit', 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '3']
hero_dict['npc_dota_hero_arc_warden'] = ['arc_warden', 'neuter', 'ranged', 'agi', 'carry', 'escape', 'nuker', '3']
hero_dict['npc_dota_hero_elder_titan'] = ['elder_titan', 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_tusk'] = ['tusk', 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', '2']
hero_dict['npc_dota_hero_winter_wyvern'] = ['winter_wyvern', 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ember_spirit'] = ['ember_spirit', 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_oracle'] = ['oracle', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'escape', '3']
hero_dict['npc_dota_hero_phoenix'] = ['phoenix', 'neuter', 'ranged', 'str', 'initiator', 'support', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_skywrath_mage'] = ['skywrath_mage', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_terrorblade'] = ['terrorblade', 'male', 'melee', 'agi', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_monkey_king'] = ['monkey_king', 'male', 'melee', 'agi', 'initiator', 'carry', 'escape', 'disabler', '2']

hero_names = ['npc_dota_hero_rattletrap', 'npc_dota_hero_furion', 'npc_dota_hero_nevermore', 'npc_dota_hero_winter_wyvern', 'npc_dota_hero_mirana', 'npc_dota_hero_batrider', 'npc_dota_hero_windrunner', 'npc_dota_hero_oracle', 
			'npc_dota_hero_sven', 'npc_dota_hero_shadow_demon', 'npc_dota_hero_vengefulspirit', 'npc_dota_hero_skywrath_mage', 'npc_dota_hero_skeleton_king', 'npc_dota_hero_naga_siren', 'npc_dota_hero_doom_bringer', 
			'npc_dota_hero_treant', 'npc_dota_hero_venomancer', 'npc_dota_hero_abyssal_underlord', 'npc_dota_hero_ursa', 'npc_dota_hero_huskar', 'npc_dota_hero_bounty_hunter', 'npc_dota_hero_elder_titan',
			'npc_dota_hero_templar_assassin', 'npc_dota_hero_death_prophet', 'npc_dota_hero_drow_ranger', 'npc_dota_hero_pugna', 'npc_dota_hero_lycan', 
			'npc_dota_hero_life_stealer', 'npc_dota_hero_morphling', 'npc_dota_hero_monkey_king','npc_dota_hero_leshrac', 'npc_dota_hero_antimage', 'npc_dota_hero_enigma', 'npc_dota_hero_medusa', 
			'npc_dota_hero_razor', 'npc_dota_hero_tiny', 'npc_dota_hero_chen', 'npc_dota_hero_bloodseeker', 'npc_dota_hero_undying', 'npc_dota_hero_shadow_shaman', 'npc_dota_hero_bane', 'npc_dota_hero_lone_druid', 
			'npc_dota_hero_centaur', 'npc_dota_hero_keeper_of_the_light', 'npc_dota_hero_enchantress', 'npc_dota_hero_rubick',  'npc_dota_hero_phantom_lancer', 'npc_dota_hero_tinker', 
			'npc_dota_hero_sniper', 'npc_dota_hero_lich', 'npc_dota_hero_puck', 'npc_dota_hero_invoker', 'npc_dota_hero_dark_seer', 'npc_dota_hero_lion', 'npc_dota_hero_kunkka', 'npc_dota_hero_arc_warden', 
			'npc_dota_hero_nyx_assassin', 'npc_dota_hero_broodmother', 'npc_dota_hero_viper', 'npc_dota_hero_luna', 'npc_dota_hero_meepo', 'npc_dota_hero_axe', 'npc_dota_hero_earthshaker', 'npc_dota_hero_techies', 
			'npc_dota_hero_juggernaut', 'npc_dota_hero_visage', 'npc_dota_hero_ancient_apparition', 'npc_dota_hero_chaos_knight', 'npc_dota_hero_spirit_breaker', 'npc_dota_hero_beastmaster',
			'npc_dota_hero_legion_commander', 'npc_dota_hero_abaddon', 'npc_dota_hero_jakiro', 'npc_dota_hero_ember_spirit', 'npc_dota_hero_alchemist', 'npc_dota_hero_pudge', 'npc_dota_hero_omniknight', 'npc_dota_hero_terrorblade', 
			'npc_dota_hero_slark', 'npc_dota_hero_warlock', 'npc_dota_hero_storm_spirit', 'npc_dota_hero_troll_warlord', 'npc_dota_hero_clinkz', 'npc_dota_hero_night_stalker', 'npc_dota_hero_slardar', 'npc_dota_hero_queenofpain',
			 'npc_dota_hero_zuus', 'npc_dota_hero_dazzle', 'npc_dota_hero_dragon_knight', 'npc_dota_hero_phantom_assassin', 'npc_dota_hero_riki', 'npc_dota_hero_tusk', 'npc_dota_hero_spectre', 
			 'npc_dota_hero_bristleback', 'npc_dota_hero_tidehunter', 'npc_dota_hero_witch_doctor', 'npc_dota_hero_sand_king', 'npc_dota_hero_lina', 'npc_dota_hero_phoenix', 'npc_dota_hero_weaver', 'npc_dota_hero_gyrocopter', 
			 'npc_dota_hero_crystal_maiden', 'npc_dota_hero_brewmaster', 'npc_dota_hero_necrolyte', 'npc_dota_hero_silencer', 'npc_dota_hero_earth_spirit', 'npc_dota_hero_disruptor', 'npc_dota_hero_faceless_void',
			 'npc_dota_hero_ogre_magi', 'npc_dota_hero_obsidian_destroyer', 'npc_dota_hero_magnataur', 'npc_dota_hero_shredder', 'npc_dota_hero_wisp']

regular_hero_names = ['winter_wyvern', 'mirana', 'batrider', 'oracle', 'sven', 'shadow_demon', 'vengefulspirit', 'skywrath_mage', 'skeleton_king', 'naga_siren', 'doom_bringer', 'treant', 'venomancer', 'abyssal_underlord', 'io', 'ursa', 'huskar', 'bounty_hunter', 'elder_titan', 'templar_assassin', 'death_prophet', 'drow_ranger', 'outworld devourer', 'shadow fiend', 'pugna', 'lycan', 'life_stealer', 'morphling', 'monkey_king', 'timbersaw', 'leshrac', 'antimage', 'enigma', 'medusa', 'razor', 'tiny', 'chen', 'bloodseeker', 'undying', 'shadow_shaman', 'bane', 'lone_druid', 'centaur warrunner', 'keeper_of_the_light', 'enchantress', 'rubick', 'necrophos', 'magnus', 'phantom_lancer', 'tinker', 'sniper', 'lich', 'puck', 'invoker', 'dark_seer', 'clockwerk', 'lion', 'kunkka', 'arc_warden', 'nyx_assassin', 'broodmother', 'viper', 'luna', 'meepo', 'axe', 'earthshaker', 'techies', 'juggernaut', 'visage', 'natures prophet', 'ancient_apparition', 'chaos_knight', 'spirit_breaker', 'beastmaster', 'legion_commander', 'abaddon', 'jakiro', 'ember_spirit', 'alchemist', 'pudge', 'omniknight', 'terrorblade', 'slark', 'warlock', 'storm_spirit', 'troll_warlord', 'clinkz', 'night_stalker', 'slardar', 'queenofpain', 'zeus', 'dazzle', 'dragon_knight', 'phantom_assassin', 'windranger', 'riki', 'tusk', 'spectre', 'bristleback', 'tidehunter', 'witch_doctor', 'sand_king', 'lina', 'phoenix', 'weaver', 'gyrocopter', 'crystal_maiden', 'brewmaster', 'silencer', 'earth_spirit', 'disruptor', 'faceless_void', 'ogre_magi']

abbreviated_hero_names = ['ww', 'sd', 'venge', 'skywrath', 'wk', 'naga', 'doom', 'veno', 'abyssal', 'wisp', 'bh', 'bounty', 'titan', 'ta', 'dp', 'drow', 'od', 'sf', 'shadow', 'ls', 'morph', 'mk', 'monkey', 'timer', 'saw', 'am', 'dusa', 'tony', 'bs', 'blood', 'ss', 'cent', 'kotl', 'ench', 'mag', 'pl', 'ds', 'clock', 'arc', 'nyx', 'brood', 'es', 'jugg', 'tb', 'np', 'natures', 'aa', 'ck', 'chaos', 'sb', 'lc', 'abby', 'jak', 'alch', 'omni', 'troll', 'ns', 'qop', 'dk', 'pa', 'tide', 'wd', 'sk', 'gyro', 'cm', 'crystal', 'brew', 'faceless', 'ogre']

old_names = ['rattletrap', 'nevermore', 'furion', 'windrunner', 'rikimaru', 'naix', 'rylai', 'magina', 'atropos', 'potm', 'lyralei', 'alleria', 'rhasta', 'lesale', 'leoric', 'lanaya', 'gondar', 'rooftrellen', 'dirge', 'slithice', 'ezalor', 'tuskar', 'tuskarr', 'mogul', 'trax', 'levi', 'crix', 'luci', 'krob', 'darchrow']

old_items = ['buriza', 'lothars', 'stygian', 'guinsoo', 'guinsoos', 'eaglehorn']

regular_items = ['clarity', 'town portal scroll', 'faerie fire', 'enchanted mango', 'healing salve', 'tome of knowledge', 'flying courier', 'smoke of deceit', 'observer ward', 'animal courier', 'sentry ward', 'tango', 'dust of appearance', 'bottle', 'iron branch', 'mantle of intelligence', 'circlet', 'belt of strength', 'blade of alacrity', 'staff of wizardry', 'gauntlets of strength', 'slippers of agility', 'band of elvenskin', 'robe of the magi', 'ogre club', 'ring of protection', 'stout shield', 'quelling blade', 'infused raindrop', 'orb of venom', 'blades of attack', 'quarterstaff', 'broadsword', 'javelin', 'blight stone', 'chainmail', 'helm of iron will', 'claymore', 'mithril hammer', 'magic stick', 'ring of regen', 'boots of speed', 'cloak', 'void stone', 'morbid mask', 'ghost scepter', 'wind lace', 'sages mask', 'gloves of haste', 'ring of health', 'gem of true sight', 'shadow amulet', 'blink dagger']

slang_items = ['tp', 'mango', 'salve', 'tome', 'up cour', 'smoke', 'ward', 'dust', 'raindrop', 'oov', 'boots', 'brown boots', 'blink', 'gem']

#---------------------------------------------------------------------- 
# tag_dict is a dictionary whose keys are tags and whose 
# values are lists of heroes that are marked with that tag
#---------------------------------------------------------------------- 

tag_dict = {}
length_by_tag = {}
chats_by_tag = {}

for t in h_tags:
  tag_dict[t] = []
  for (h,tag_list) in list(hero_dict.items()):
    if t in tag_list:
      tag_dict[t] += [h]


      # Creates a list [gender, support/carry/none, difficulty] for a given hero
def create_type(hero):
    list = ["", "", ""]
    if hero != "null":
        list[0] = hero_dict[hero][1]
        list[2] = hero_dict[hero][len(hero_dict[hero]) - 1]
        if "carry" in hero_dict[hero]:
            if "support" in hero_dict[hero]:
                list[1] = "none"
            else:
                list[1] = "carry"
        elif "support" in hero_dict[hero]:
            list[1] = "support"
        else:
            list[1] = "none"
    return list