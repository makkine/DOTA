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
          'jungler',  'melee',  'nuker', 'pusher', 'ranged', 'support']

difficulty_tags = ['1', '2', '3']
gender_tags = ['female', 'male', 'neuter']
skill_tags = ['agi', 'int', 'str']
hero_names = ['am', 'axe', 'bane', 'cm', 'dr', 'es', 'jn', 'mirana', 'nm', 'ml', 'pl', 'puck', 'pudge', 'razor', 'sk',
              ]


hero_dict = {}
hero_dict['npc_dota_hero_antimage'] = ['am','male', 'melee', 'agi', 'carry', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_axe'] = ['axe','male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'jungler', '1']
hero_dict['npc_dota_hero_bane'] = ['bane','male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'durable', '2']
hero_dict['npc_dota_hero_bloodseeker'] = ['bs','male', 'melee', 'agi', 'carry', 'disabler', 'nuker', 'jungler', 'initiator', '1']
hero_dict['npc_dota_hero_crystal_maiden'] = ['cm', 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '1']
hero_dict['npc_dota_hero_drow_ranger'] = ['dr', 'female', 'ranged', 'agi', 'carry', 'disabler', 'pusher', '1']
hero_dict['npc_dota_hero_earthshaker'] = ['es','male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker', "2"]
hero_dict['npc_dota_hero_juggernaut'] = ['jn', 'male', 'melee', 'agi', 'carry', 'pusher', 'escape', '1']
hero_dict['npc_dota_hero_mirana'] = ['mirana', 'female', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'support', 'disabler', '2']
hero_dict['npc_dota_hero_nevermore'] = ['nm', 'male', 'ranged', 'agi', 'carry', 'nuker', '2']
hero_dict['npc_dota_hero_morphling'] = ['ml','male', 'ranged', 'agi', 'carry', 'escape', 'nuker', 'durable', 'disabler', '3']
hero_dict['npc_dota_hero_phantom_lancer'] = ['pl', 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_puck'] = ['puck','female', 'ranged', 'int', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_pudge'] = ['pudge', 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_razor'] = ['razor','male', 'ranged', 'agi', 'carry', 'durable', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_sand_king'] = ['sk', 'male', 'melee', 'str', 'initiator', 'escape', 'disabler', 'nuker', 'jungler', '2']
hero_dict['npc_dota_hero_storm_spirit'] = ['ss','male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'initiator', 'escape', '3']
hero_dict['npc_dota_hero_sven'] = ['sven', 'male', 'melee', 'str', 'carry', 'durable', 'disabler', 'initiator', 'nuker', '1']
hero_dict['npc_dota_hero_tiny'] = ['tiny', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'pusher', 'durable']
hero_dict['npc_dota_hero_vengefulspirit'] = ['vs', 'female', 'ranged', 'agi', 'support', 'escape', 'nuker', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_windrunner'] = ['wr', 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_zuus'] = ['zuus', 'male', 'ranged', 'int', 'nuker', '1']
hero_dict['npc_dota_hero_kunkka'] = ['kunkka','male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_lina'] = ['lina', 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', '1']
hero_dict['npc_dota_hero_lich'] = ['lich', 'male', 'ranged', 'int', 'support', 'nuker', '1']
hero_dict['npc_dota_hero_lion'] = ['lion', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '1']
hero_dict['npc_dota_hero_shadow_shaman'] = ['shs', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'initiator', '1']
hero_dict['npc_dota_hero_slardar'] = ['slardar', 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_tidehunter'] = ['th', 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_witch_doctor'] = ['wd', 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_riki'] = ['riki', 'male', 'melee', 'agi', 'carry', 'escape', 'disabler', '1']
hero_dict['npc_dota_hero_enigma'] = ["l", 'male', 'ranged', 'int', 'pusher', 'disabler', 'initiator', 'jungler', '2']
hero_dict['npc_dota_hero_tinker'] = ["l", 'male', 'ranged', 'int', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_sniper'] = ["l", 'male', 'ranged', 'agi', 'carry', 'nuker', '1']
hero_dict['npc_dota_hero_necrolyte'] = ["l", 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_warlock'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'initiator', '1']
hero_dict['npc_dota_hero_beastmaster'] = ["l", 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_queenofpain'] = ["l", 'female', 'ranged', 'int', 'carry', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_venomancer'] = ["l", 'male', 'ranged', 'agi', 'support', 'initiator', 'nuker', 'pusher', 'disabler', '1']
hero_dict['npc_dota_hero_faceless_void'] = ["l", 'male', 'melee', 'agi', 'carry', 'escape', 'initiator', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_skeleton_king'] = ["l", 'male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'carry']
hero_dict['npc_dota_hero_death_prophet'] = ["l", 'female', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_phantom_assassin'] = ["l", 'female', 'melee', 'agi', 'carry', 'escape', '1']
hero_dict['npc_dota_hero_pugna'] = ["l", 'male', 'ranged', 'int', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_templar_assassin'] = ["l", 'female', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_viper'] = ["l", 'male', 'ranged', 'agi', 'carry', 'durable', 'initiator', 'disabler', '1']
hero_dict['npc_dota_hero_luna'] = ["l", 'female', 'ranged', 'agi', 'carry', 'pusher', 'nuker', '1']
hero_dict['npc_dota_hero_dragon_knight'] = ["l", 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable', 'pusher']
hero_dict['npc_dota_hero_dazzle'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_rattletrap'] = ["l", 'male', 'melee', 'str', 'initiator', 'durable', 'disabler', 'nuker']
hero_dict['npc_dota_hero_leshrac'] = ["l", 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'support', 'pusher', '1']
hero_dict['npc_dota_hero_furion'] = ["l", 'male', 'ranged', 'int', 'carry', 'escape', 'nuker', 'jungler', 'pusher', '2']
hero_dict['npc_dota_hero_life_stealer'] = ["l", 'male', 'melee', 'str', 'durable', 'jungler', 'disabler', 'carry', 'escape']
hero_dict['npc_dota_hero_dark_seer'] = ["l", 'male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_clinkz'] = ["l", 'male', 'ranged', 'agi', 'carry', 'escape', 'pusher', '2']
hero_dict['npc_dota_hero_omniknight'] = ["l", 'male', 'melee', 'str', 'durable', 'support', 'nuker']
hero_dict['npc_dota_hero_enchantress'] = ["l", 'female', 'ranged', 'int', 'support', 'disabler', 'pusher', 'jungler', 'durable', '2']
hero_dict['npc_dota_hero_huskar'] = ["l", 'male', 'ranged', 'str', 'initiator', 'carry', 'durable']
hero_dict['npc_dota_hero_night_stalker'] = ["l", 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_broodmother'] = ["l", 'female', 'melee', 'agi', 'carry', 'escape', 'nuker', 'pusher', '2']
hero_dict['npc_dota_hero_bounty_hunter'] = ["l", 'male', 'melee', 'agi', 'escape', 'nuker', '1']
hero_dict['npc_dota_hero_weaver'] = ["l", 'male', 'ranged', 'agi', 'carry', 'escape', '2']
hero_dict['npc_dota_hero_jakiro'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', '1']
hero_dict['npc_dota_hero_batrider'] = ["l", 'male', 'ranged', 'int', 'initiator', 'disabler', 'escape', 'jungler', '2']
hero_dict['npc_dota_hero_chen'] = ["l", 'male', 'ranged', 'int', 'support', 'pusher', 'jungler', '3']
hero_dict['npc_dota_hero_spectre'] = ["l", 'female', 'melee', 'agi', 'carry', 'escape', 'durable', '2']
hero_dict['npc_dota_hero_doom_bringer'] = ["l", 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_ancient_apparition'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ursa'] = ["l", 'male', 'melee', 'agi', 'carry', 'jungler', 'durable', 'disabler', '1']
hero_dict['npc_dota_hero_spirit_breaker'] = ["l", 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'escape']
hero_dict['npc_dota_hero_gyrocopter'] = ["l", 'male', 'ranged', 'agi', 'carry', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_alchemist'] = ["l", 'male', 'melee', 'str', 'initiator', 'support', 'disabler', 'nuker', 'carry', 'durable']
hero_dict['npc_dota_hero_invoker'] = ["l", 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', 'escape', 'pusher', '3']
hero_dict['npc_dota_hero_silencer'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'carry', 'initiator', '2']
hero_dict['npc_dota_hero_obsidian_destroyer'] = ["l", 'male', 'ranged', 'int', 'carry', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_lycan'] = ["l", 'male', 'melee', 'str', 'carry', 'pusher', 'jungler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_brewmaster'] = ["l", 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'nuker', 'durable']
hero_dict['npc_dota_hero_shadow_demon'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_lone_druid'] = ["l", 'male', 'ranged', 'agi', 'carry', 'pusher', 'jungler', 'durable', '3']
hero_dict['npc_dota_hero_meepo'] = ["l", 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', 'pusher', '3']
hero_dict['npc_dota_hero_keeper_of_the_light'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'jungler', '2']
hero_dict['npc_dota_hero_visage'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'pusher', 'durable', '3']
hero_dict['npc_dota_hero_disruptor'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'initiator', '2']
hero_dict['npc_dota_hero_rubick'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '3']
hero_dict['npc_dota_hero_ogre_magi'] = ["l", 'male', 'melee', 'int', 'support', 'disabler', 'nuker', 'durable', 'initiator', '1']
hero_dict['npc_dota_hero_nyx_assassin'] = ["l", 'male', 'melee', 'agi', 'disabler', 'initiator', 'escape', 'nuker', '2']
hero_dict['npc_dota_hero_naga_siren'] = ["l", 'female', 'melee', 'agi', 'carry', 'escape', 'support', 'pusher', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_undying'] = ["l", 'male', 'melee', 'str', 'nuker', 'support', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_chaos_knight'] = ["l", 'male', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'pusher', '1']
hero_dict['npc_dota_hero_wisp'] = ["l", 'neuter', 'ranged', 'str', 'escape', 'support', 'nuker', '3']
hero_dict['npc_dota_hero_treant'] = ["l", 'male', 'melee', 'str', 'initiator', 'support', 'disabler', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_magnataur'] = ["l", 'male', 'melee', 'str', 'initiator', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_centaur'] = ["l", 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '1']
hero_dict['npc_dota_hero_slark'] = ["l", 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', '1']
hero_dict['npc_dota_hero_shredder'] = ["l", 'male', 'melee', 'str', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_medusa'] = ["l", 'female', 'ranged', 'agi', 'carry', 'disabler', 'durable', '1']
hero_dict['npc_dota_hero_troll_warlord'] = ["l", 'male', 'ranged', 'agi', 'carry', 'pusher', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_techies'] = ["l", 'male', 'ranged', 'int', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_abaddon'] = ["l", 'male', 'melee', 'str', 'carry', 'support', 'durable', '1']
hero_dict['npc_dota_hero_bristleback'] = ["l", 'male', 'melee', 'str', 'initiator', 'carry', 'nuker', 'durable', '1']
hero_dict['npc_dota_hero_abyssal_underlord'] = ["l", 'male', 'melee', 'str', 'support', 'disabler', 'nuker', 'durable', 'escape', '2']
hero_dict['npc_dota_hero_legion_commander'] = ["l", 'female', 'melee', 'str', 'initiator', 'carry', 'disabler', 'durable', 'nuker', '1']
hero_dict['npc_dota_hero_earth_spirit'] = ["l", 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', 'escape', '3']
hero_dict['npc_dota_hero_arc_warden'] = ["l", 'neuter', 'ranged', 'agi', 'carry', 'escape', 'nuker', '3']
hero_dict['npc_dota_hero_elder_titan'] = ["l", 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', 'durable', '2']
hero_dict['npc_dota_hero_tusk'] = ["l", 'male', 'melee', 'str', 'initiator', 'nuker', 'disabler', '2']
hero_dict['npc_dota_hero_winter_wyvern'] = ["l", 'female', 'ranged', 'int', 'support', 'disabler', 'nuker', '2']
hero_dict['npc_dota_hero_ember_spirit'] = ["l", 'male', 'melee', 'agi', 'carry', 'escape', 'nuker', 'disabler', 'initiator', '2']
hero_dict['npc_dota_hero_oracle'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', 'escape', '3']
hero_dict['npc_dota_hero_phoenix'] = ["l", 'neuter', 'ranged', 'str', 'initiator', 'support', 'disabler', 'nuker', 'escape', '2']
hero_dict['npc_dota_hero_skywrath_mage'] = ["l", 'male', 'ranged', 'int', 'support', 'disabler', 'nuker', '1']
hero_dict['npc_dota_hero_terrorblade'] = ["l", 'male', 'melee', 'agi', 'carry', 'pusher', 'nuker', '2']
hero_dict['npc_dota_hero_monkey_king'] = ["l", 'male', 'melee', 'agi', 'initiator', 'carry', 'escape', 'disabler', '2']

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