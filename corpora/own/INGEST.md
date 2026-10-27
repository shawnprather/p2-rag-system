# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 353 (the final check needs at least 200)
- Words: 507,751
- Estimated tokens (words times 1.4): 710,851 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `2d-2d_antialiasing` | 517 | - | - | - |
| `2d-2d_lights_and_shadows` | 2,586 | - | - | - |
| `2d-2d_movement` | 939 | - | - | - |
| `2d-2d_parallax` | 1,624 | - | - | - |
| `2d-2d_sprite_animation` | 1,160 | - | - | - |
| `2d-2d_transforms` | 571 | - | - | - |
| `2d-canvas_layers` | 432 | - | - | - |
| `2d-custom_drawing_in_2d` | 4,336 | - | - | - |
| `2d-introduction_to_2d` | 2,618 | - | - | - |
| `2d-particle_process_material_2d` | 1,122 | - | - | - |
| `2d-using_tilemaps` | 2,388 | - | - | - |
| `2d-using_tilesets` | 3,365 | - | - | - |
| `3d-3d_antialiasing` | 2,066 | - | - | - |
| `3d-3d_rendering_limitations` | 960 | - | - | - |
| `3d-3d_text` | 1,064 | - | - | - |
| `3d-environment_and_post_processing` | 6,590 | - | - | - |
| `3d-global_illumination-faking_global_illumination` | 726 | - | - | - |
| `3d-global_illumination-introduction_to_global_illumination` | 2,375 | - | - | - |
| `3d-global_illumination-reflection_probes` | 1,139 | - | - | - |
| `3d-global_illumination-using_lightmap_gi` | 4,321 | - | - | - |
| `3d-global_illumination-using_sdfgi` | 1,782 | - | - | - |
| `3d-global_illumination-using_voxel_gi` | 1,592 | - | - | - |
| `3d-introduction_to_3d` | 2,699 | - | - | - |
| `3d-lights_and_shadows` | 4,500 | - | - | - |
| `3d-mesh_lod` | 1,119 | - | - | - |
| `3d-occlusion_culling` | 1,890 | - | - | - |
| `3d-particles-attractors` | 974 | - | - | - |
| `3d-particles-collision` | 1,205 | - | - | - |
| `3d-particles-complex_shapes` | 603 | - | - | - |
| `3d-particles-creating_a_3d_particle_system` | 498 | - | - | - |
| `3d-particles-process_material_properties` | 2,998 | - | - | - |
| `3d-particles-properties` | 1,426 | - | - | - |
| `3d-particles-subemitters` | 507 | - | - | - |
| `3d-particles-trails` | 868 | - | - | - |
| `3d-particles-turbulence` | 650 | - | - | - |
| `3d-physical_light_and_camera_units` | 1,892 | - | - | - |
| `3d-procedural_geometry-arraymesh` | 1,958 | - | - | - |
| `3d-procedural_geometry-immediatemesh` | 465 | - | - | - |
| `3d-procedural_geometry-meshdatatool` | 988 | - | - | - |
| `3d-procedural_geometry-surfacetool` | 811 | - | - | - |
| `3d-resolution_scaling` | 1,487 | - | - | - |
| `3d-spring_arm` | 591 | - | - | - |
| `3d-standard_material_3d` | 4,872 | - | - | - |
| `3d-using_decals` | 1,861 | - | - | - |
| `3d-using_gridmaps` | 1,333 | - | - | - |
| `3d-using_transforms` | 2,336 | - | - | - |
| `3d-variable_rate_shading` | 1,110 | - | - | - |
| `3d-visibility_ranges` | 1,760 | - | - | - |
| `3d-volumetric_fog` | 2,224 | - | - | - |
| `animation-animation_track_types` | 1,137 | - | - | - |
| `animation-animation_tree` | 3,082 | - | - | - |
| `animation-creating_movies` | 3,233 | - | - | - |
| `animation-introduction` | 1,944 | - | - | - |
| `animation-playing_videos` | 2,444 | - | - | - |
| `assets_pipeline-exporting_3d_scenes` | 151 | - | - | - |
| `assets_pipeline-import_process` | 834 | - | - | - |
| `assets_pipeline-importing_3d_scenes-advanced_import_settings` | 1,570 | - | - | - |
| `assets_pipeline-importing_3d_scenes-available_formats` | 1,405 | - | - | - |
| `assets_pipeline-importing_3d_scenes-import_configuration` | 2,771 | - | - | - |
| `assets_pipeline-importing_3d_scenes-model_export_considerations` | 624 | - | - | - |
| `assets_pipeline-importing_3d_scenes-node_type_customization` | 940 | - | - | - |
| `assets_pipeline-importing_audio_samples` | 1,775 | - | - | - |
| `assets_pipeline-importing_images` | 3,896 | - | - | - |
| `assets_pipeline-importing_translations` | 301 | - | - | - |
| `assets_pipeline-retargeting_3d_skeletons` | 999 | - | - | - |
| `audio-audio_buses` | 801 | - | - | - |
| `audio-audio_effects` | 1,874 | - | - | - |
| `audio-text_to_speech` | 847 | - | - | - |
| `best_practices-autoloads_versus_regular_nodes` | 743 | - | - | - |
| `best_practices-godot_interfaces` | 2,186 | - | - | - |
| `best_practices-godot_notifications` | 1,475 | - | - | - |
| `best_practices-introduction_best_practices` | 180 | - | - | - |
| `best_practices-logic_preferences` | 1,265 | - | - | - |
| `best_practices-node_alternatives` | 444 | - | - | - |
| `best_practices-project_organization` | 689 | - | - | - |
| `best_practices-scene_organization` | 2,313 | - | - | - |
| `best_practices-scenes_versus_scripts` | 1,115 | - | - | - |
| `best_practices-version_control_systems` | 971 | - | - | - |
| `best_practices-what_are_godot_classes` | 448 | - | - | - |
| `editor-command_line_tutorial` | 2,873 | - | - | - |
| `editor-customizing_editor` | 1,023 | - | - | - |
| `editor-external_editor` | 588 | - | - | - |
| `editor-game_embedding` | 1,728 | - | - | - |
| `editor-inspector_dock` | 899 | - | - | - |
| `editor-project_manager` | 1,029 | - | - | - |
| `editor-project_settings` | 534 | - | - | - |
| `editor-script_editor` | 3,275 | - | - | - |
| `editor-using_engine_compilation_configuration_editor` | 562 | - | - | - |
| `editor-using_the_android_editor` | 527 | - | - | - |
| `editor-using_the_xr_editor` | 526 | - | - | - |
| `export-android_gradle_build` | 465 | - | - | - |
| `export-changing_application_icon_for_windows` | 448 | - | - | - |
| `export-exporting_for_android` | 1,143 | - | - | - |
| `export-exporting_for_dedicated_servers` | 1,513 | - | - | - |
| `export-exporting_for_ios` | 946 | - | - | - |
| `export-exporting_for_linux` | 528 | - | - | - |
| `export-exporting_for_macos` | 1,547 | - | - | - |
| `export-exporting_for_web` | 2,908 | - | - | - |
| `export-exporting_for_windows` | 691 | - | - | - |
| `export-exporting_pcks` | 1,716 | - | - | - |
| `export-exporting_projects` | 1,640 | - | - | - |
| `export-feature_tags` | 877 | - | - | - |
| `export-one-click_deploy` | 1,211 | - | - | - |
| `export-running_on_macos` | 630 | - | - | - |
| `getting_started-first_2d_game-01.project_setup` | 339 | - | - | - |
| `getting_started-first_2d_game-02.player_scene` | 785 | - | - | - |
| `getting_started-first_2d_game-03.coding_the_player` | 1,914 | - | - | - |
| `getting_started-first_2d_game-04.creating_the_enemy` | 632 | - | - | - |
| `getting_started-first_2d_game-05.the_main_game_scene` | 1,367 | - | - | - |
| `getting_started-first_2d_game-06.heads_up_display` | 1,197 | - | - | - |
| `getting_started-first_2d_game-07.finishing-up` | 685 | - | - | - |
| `getting_started-first_3d_game-01.game_setup` | 878 | - | - | - |
| `getting_started-first_3d_game-02.player_input` | 870 | - | - | - |
| `getting_started-first_3d_game-03.player_movement_code` | 1,974 | - | - | - |
| `getting_started-first_3d_game-04.mob_scene` | 1,664 | - | - | - |
| `getting_started-first_3d_game-05.spawning_mobs` | 1,559 | - | - | - |
| `getting_started-first_3d_game-06.jump_and_squash` | 1,785 | - | - | - |
| `getting_started-first_3d_game-07.killing_player` | 2,055 | - | - | - |
| `getting_started-first_3d_game-08.score_and_replay` | 1,898 | - | - | - |
| `getting_started-first_3d_game-09.adding_animations` | 2,557 | - | - | - |
| `getting_started-first_3d_game-going_further` | 264 | - | - | - |
| `getting_started-introduction-first_look_at_the_editor` | 836 | - | - | - |
| `getting_started-introduction-godot_design_philosophy` | 1,160 | - | - | - |
| `getting_started-introduction-introduction_to_godot` | 590 | - | - | - |
| `getting_started-introduction-key_concepts_overview` | 547 | - | - | - |
| `getting_started-introduction-learn_to_code_with_gdscript` | 185 | - | - | - |
| `getting_started-introduction-learning_new_features` | 972 | - | - | - |
| `getting_started-step_by_step-instancing` | 1,455 | - | - | - |
| `getting_started-step_by_step-nodes_and_scenes` | 1,082 | - | - | - |
| `getting_started-step_by_step-scripting_first_script` | 1,469 | - | - | - |
| `getting_started-step_by_step-scripting_languages` | 903 | - | - | - |
| `getting_started-step_by_step-scripting_player_input` | 936 | - | - | - |
| `getting_started-step_by_step-signals` | 2,180 | - | - | - |
| `i18n-internationalizing_games` | 2,308 | - | - | - |
| `i18n-locales` | 2,514 | - | - | - |
| `i18n-localization_using_gettext` | 1,777 | - | - | - |
| `i18n-localization_using_spreadsheets` | 757 | - | - | - |
| `i18n-pseudolocalization` | 514 | - | - | - |
| `inputs-controller_features` | 1,355 | - | - | - |
| `inputs-controllers_gamepads_joysticks` | 2,119 | - | - | - |
| `inputs-custom_mouse_cursor` | 398 | - | - | - |
| `inputs-handling_quit_requests` | 401 | - | - | - |
| `inputs-input_examples` | 1,418 | - | - | - |
| `inputs-inputevent` | 1,471 | - | - | - |
| `inputs-mouse_and_input_coordinates` | 267 | - | - | - |
| `io-background_loading` | 403 | - | - | - |
| `io-data_paths` | 943 | - | - | - |
| `io-runtime_file_loading_and_saving` | 1,919 | - | - | - |
| `io-saving_games` | 1,820 | - | - | - |
| `math-beziers_and_curves` | 1,190 | - | - | - |
| `math-interpolation` | 686 | - | - | - |
| `math-matrices_and_transforms` | 3,608 | - | - | - |
| `math-random_number_generation` | 2,806 | - | - | - |
| `math-vector_math` | 1,930 | - | - | - |
| `math-vectors_advanced` | 2,287 | - | - | - |
| `migrating-upgrading_to_godot_4` | 3,956 | - | - | - |
| `migrating-upgrading_to_godot_4.1` | 1,216 | - | - | - |
| `migrating-upgrading_to_godot_4.2` | 1,511 | - | - | - |
| `migrating-upgrading_to_godot_4.3` | 1,890 | - | - | - |
| `migrating-upgrading_to_godot_4.4` | 1,214 | - | - | - |
| `migrating-upgrading_to_godot_4.5` | 1,949 | - | - | - |
| `migrating-upgrading_to_godot_4.6` | 1,628 | - | - | - |
| `migrating-upgrading_to_godot_4.7` | 1,611 | - | - | - |
| `navigation-navigation_connecting_navmesh` | 400 | - | - | - |
| `navigation-navigation_debug_tools` | 508 | - | - | - |
| `navigation-navigation_different_actor_area_access` | 204 | - | - | - |
| `navigation-navigation_different_actor_locomotion` | 236 | - | - | - |
| `navigation-navigation_different_actor_types` | 653 | - | - | - |
| `navigation-navigation_introduction_2d` | 1,128 | - | - | - |
| `navigation-navigation_introduction_3d` | 1,107 | - | - | - |
| `navigation-navigation_optimizing_performance` | 1,419 | - | - | - |
| `navigation-navigation_using_navigationagents` | 2,931 | - | - | - |
| `navigation-navigation_using_navigationlayers` | 774 | - | - | - |
| `navigation-navigation_using_navigationlinks` | 783 | - | - | - |
| `navigation-navigation_using_navigationmaps` | 416 | - | - | - |
| `navigation-navigation_using_navigationmeshes` | 3,228 | - | - | - |
| `navigation-navigation_using_navigationobstacles` | 1,405 | - | - | - |
| `navigation-navigation_using_navigationpathqueryobjects` | 1,811 | - | - | - |
| `navigation-navigation_using_navigationpaths` | 873 | - | - | - |
| `navigation-navigation_using_navigationregions` | 479 | - | - | - |
| `navigation-navigation_using_navigationservers` | 1,022 | - | - | - |
| `networking-high_level_multiplayer` | 3,586 | - | - | - |
| `networking-http_request_class` | 640 | - | - | - |
| `networking-ssl_certificates` | 395 | - | - | - |
| `networking-websocket` | 816 | - | - | - |
| `performance-cpu_optimization` | 1,858 | - | - | - |
| `performance-general_optimization` | 1,733 | - | - | - |
| `performance-gpu_optimization` | 2,194 | - | - | - |
| `performance-optimizing_3d_performance` | 1,251 | - | - | - |
| `performance-pipeline_compilations` | 2,221 | - | - | - |
| `performance-thread_safe_apis` | 787 | - | - | - |
| `performance-using_multiple_threads` | 1,368 | - | - | - |
| `performance-using_servers` | 1,665 | - | - | - |
| `physics-collision_shapes_2d` | 864 | - | - | - |
| `physics-collision_shapes_3d` | 886 | - | - | - |
| `physics-interpolation-2d_and_3d_physics_interpolation` | 168 | - | - | - |
| `physics-interpolation-advanced_physics_interpolation` | 1,101 | - | - | - |
| `physics-interpolation-physics_interpolation_introduction` | 1,751 | - | - | - |
| `physics-interpolation-physics_interpolation_quick_start_guide` | 92 | - | - | - |
| `physics-interpolation-using_physics_interpolation` | 1,105 | - | - | - |
| `physics-kinematic_character_2d` | 1,036 | - | - | - |
| `physics-large_world_coordinates` | 1,664 | - | - | - |
| `physics-physics_introduction` | 2,612 | - | - | - |
| `physics-ragdoll_system` | 1,411 | - | - | - |
| `physics-ray-casting` | 1,120 | - | - | - |
| `physics-rigid_body` | 585 | - | - | - |
| `physics-soft_body` | 991 | - | - | - |
| `physics-troubleshooting_physics_issues` | 1,574 | - | - | - |
| `physics-using_area_2d` | 738 | - | - | - |
| `physics-using_character_body_2d` | 2,229 | - | - | - |
| `physics-using_jolt_physics` | 1,737 | - | - | - |
| `platform-android-android_library` | 1,397 | - | - | - |
| `platform-android-android_plugin` | 1,936 | - | - | - |
| `platform-android-javaclasswrapper_and_androidruntimeplugin` | 839 | - | - | - |
| `platform-android-resolving_crashes_on_android` | 546 | - | - | - |
| `platform-linux-wayland_x11` | 480 | - | - | - |
| `platform-web-customizing_html5_shell` | 1,460 | - | - | - |
| `platform-web-javascript_bridge` | 1,339 | - | - | - |
| `plugins-editor-inspector_plugins` | 1,115 | - | - | - |
| `plugins-editor-installing_plugins` | 414 | - | - | - |
| `plugins-editor-internationalizing_plugins` | 220 | - | - | - |
| `plugins-editor-making_main_screen_plugins` | 1,097 | - | - | - |
| `plugins-editor-making_plugins` | 2,128 | - | - | - |
| `plugins-editor-visual_shader_plugins` | 819 | - | - | - |
| `plugins-running_code_in_the_editor` | 3,107 | - | - | - |
| `rendering-compositor` | 2,457 | - | - | - |
| `rendering-drawable_textures` | 1,459 | - | - | - |
| `rendering-hdr_output` | 2,457 | - | - | - |
| `rendering-jitter_stutter` | 2,376 | - | - | - |
| `rendering-multiple_resolutions` | 4,274 | - | - | - |
| `rendering-renderers` | 1,719 | - | - | - |
| `rendering-viewports` | 1,656 | - | - | - |
| `scripting-c_sharp-c_sharp_basics` | 2,079 | - | - | - |
| `scripting-c_sharp-c_sharp_collections` | 936 | - | - | - |
| `scripting-c_sharp-c_sharp_differences` | 2,691 | - | - | - |
| `scripting-c_sharp-c_sharp_exports` | 2,351 | - | - | - |
| `scripting-c_sharp-c_sharp_features` | 748 | - | - | - |
| `scripting-c_sharp-c_sharp_global_classes` | 402 | - | - | - |
| `scripting-c_sharp-c_sharp_signals` | 1,316 | - | - | - |
| `scripting-c_sharp-c_sharp_style_guide` | 1,325 | - | - | - |
| `scripting-c_sharp-c_sharp_variant` | 912 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0001` | 165 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0002` | 202 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0003` | 206 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0101` | 143 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0102` | 182 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0103` | 188 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0104` | 149 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0105` | 115 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0106` | 229 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0107` | 141 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0108` | 167 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0109` | 101 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0110` | 160 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0111` | 186 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0201` | 205 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0202` | 255 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0203` | 231 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0301` | 222 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0302` | 271 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0303` | 142 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0401` | 222 | - | - | - |
| `scripting-c_sharp-diagnostics-gd0402` | 161 | - | - | - |
| `scripting-change_scenes_manually` | 729 | - | - | - |
| `scripting-cpp-about_godot_cpp` | 581 | - | - | - |
| `scripting-cpp-build_system-cmake` | 1,282 | - | - | - |
| `scripting-cpp-build_system-scons` | 465 | - | - | - |
| `scripting-cpp-core_types` | 598 | - | - | - |
| `scripting-cpp-gdextension_cpp_example` | 2,945 | - | - | - |
| `scripting-cpp-gdextension_docs_system` | 642 | - | - | - |
| `scripting-creating_script_templates` | 1,047 | - | - | - |
| `scripting-cross_language_scripting` | 745 | - | - | - |
| `scripting-debug-custom_performance_monitors` | 527 | - | - | - |
| `scripting-debug-debugger_panel` | 1,462 | - | - | - |
| `scripting-debug-objectdb_profiler` | 920 | - | - | - |
| `scripting-debug-output_panel` | 708 | - | - | - |
| `scripting-debug-overview_of_debugging_tools` | 1,437 | - | - | - |
| `scripting-debug-the_profiler` | 1,153 | - | - | - |
| `scripting-evaluating_expressions` | 957 | - | - | - |
| `scripting-filesystem` | 688 | - | - | - |
| `scripting-gdscript-gdscript_advanced` | 2,071 | - | - | - |
| `scripting-gdscript-gdscript_basics` | 12,589 | - | - | - |
| `scripting-gdscript-gdscript_documentation_comments` | 1,466 | - | - | - |
| `scripting-gdscript-gdscript_exports` | 2,691 | - | - | - |
| `scripting-gdscript-gdscript_format_string` | 1,470 | - | - | - |
| `scripting-gdscript-gdscript_styleguide` | 2,962 | - | - | - |
| `scripting-gdscript-static_typing` | 2,978 | - | - | - |
| `scripting-gdscript-warning_system` | 290 | - | - | - |
| `scripting-groups` | 571 | - | - | - |
| `scripting-how_to_read_the_godot_api` | 731 | - | - | - |
| `scripting-idle_and_physics_processing` | 473 | - | - | - |
| `scripting-instancing_with_signals` | 616 | - | - | - |
| `scripting-logging` | 1,584 | - | - | reference list dropped, 826 characters (numbered entries) |
| `scripting-nodes_and_scene_instances` | 810 | - | - | - |
| `scripting-other_languages` | 96 | - | - | - |
| `scripting-overridable_functions` | 553 | - | - | - |
| `scripting-pausing_games` | 643 | - | - | - |
| `scripting-resources` | 1,920 | - | - | - |
| `scripting-scene_tree` | 970 | - | - | - |
| `scripting-scene_unique_nodes` | 559 | - | - | - |
| `scripting-singletons_autoload` | 1,420 | - | - | - |
| `shaders-advanced_postprocessing` | 1,476 | - | - | - |
| `shaders-compute_shaders` | 2,083 | - | - | - |
| `shaders-converting_glsl_to_godot_shaders` | 1,223 | - | - | - |
| `shaders-custom_postprocessing` | 807 | - | - | - |
| `shaders-introduction_to_shaders` | 1,048 | - | - | - |
| `shaders-making_trees` | 504 | - | - | - |
| `shaders-screen-reading_shaders` | 1,139 | - | - | - |
| `shaders-shader_reference-canvas_item_shader` | 1,872 | - | - | - |
| `shaders-shader_reference-fog_shader` | 481 | - | - | - |
| `shaders-shader_reference-particle_shader` | 1,100 | - | - | - |
| `shaders-shader_reference-shader_functions` | 10,162 | - | - | - |
| `shaders-shader_reference-shader_preprocessor` | 2,088 | - | - | - |
| `shaders-shader_reference-shading_language` | 5,609 | - | - | - |
| `shaders-shader_reference-sky_shader` | 1,198 | - | - | - |
| `shaders-shader_reference-spatial_shader` | 4,077 | - | - | - |
| `shaders-shader_reference-texture_blit_shader` | 475 | - | - | - |
| `shaders-shaders_style_guide` | 1,354 | - | - | - |
| `shaders-using_viewport_as_texture` | 2,040 | - | - | - |
| `shaders-visual_shaders` | 1,401 | - | - | - |
| `shaders-your_first_shader-your_first_2d_shader` | 1,327 | - | - | - |
| `shaders-your_first_shader-your_first_3d_shader` | 2,151 | - | - | - |
| `shaders-your_first_shader-your_second_3d_shader` | 1,865 | - | - | - |
| `troubleshooting` | 1,803 | - | - | - |
| `ui-bbcode_in_richtextlabel` | 5,422 | - | - | - |
| `ui-creating_applications` | 4,525 | - | - | - |
| `ui-gui_containers` | 1,230 | - | - | - |
| `ui-gui_navigation` | 519 | - | - | - |
| `ui-gui_skinning` | 1,927 | - | - | - |
| `ui-gui_theme_type_variations` | 604 | - | - | - |
| `ui-gui_using_fonts` | 5,068 | - | - | - |
| `ui-gui_using_theme_editor` | 1,074 | - | - | - |
| `ui-size_and_anchors` | 630 | - | - | - |
| `xr-a_better_xr_start_script` | 1,971 | - | - | - |
| `xr-ar_passthrough` | 935 | - | - | - |
| `xr-basic_xr_locomotion` | 819 | - | - | - |
| `xr-deploying_to_android` | 663 | - | - | - |
| `xr-introducing_xr_tools` | 653 | - | - | - |
| `xr-mobilevr_intro` | 278 | - | - | - |
| `xr-openvr_intro` | 86 | - | - | - |
| `xr-openxr_body_tracking` | 144 | - | - | - |
| `xr-openxr_composition_layers` | 1,357 | - | - | - |
| `xr-openxr_hand_tracking` | 2,603 | - | - | - |
| `xr-openxr_render_models` | 1,522 | - | - | - |
| `xr-openxr_settings` | 2,235 | - | - | - |
| `xr-openxr_spatial_entities` | 7,550 | - | - | - |
| `xr-setting_up_xr` | 1,438 | - | - | - |
| `xr-webxr_intro` | 705 | - | - | - |
| `xr-xr_action_map` | 4,324 | - | - | - |
| `xr-xr_full_screen_effects` | 455 | - | - | - |
| `xr-xr_next_steps` | 191 | - | - | - |
| `xr-xr_room_scale` | 2,586 | - | - | - |
| `xr-xr_terminology` | 553 | - | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
