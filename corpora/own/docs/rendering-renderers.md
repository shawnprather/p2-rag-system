# Overview of renderers

Overview of renderers

Seealso: This page gives an overview of Godot's renderers, focusing on the differences between their rendering features. For more technical details on the renderers, see doc_internal_rendering_architecture.
Introduction

Godot 4 includes three renderers:

Forward+. The most advanced renderer, suited for desktop platforms only.
  Used by default on desktop platforms. This renderer uses Vulkan, Direct3D 12,
  or Metal as the rendering driver, and it uses the RenderingDevice backend.
Mobile. Fewer features, but renders simple scenes faster. Suited for mobile
  and desktop platforms. Used by default on mobile platforms. This renderer uses
  Vulkan, Direct3D 12, or Metal as the rendering driver, and it uses
  the RenderingDevice backend.
Compatibility, sometimes called GL Compatibility. The least advanced
  renderer, suited for low-end desktop and mobile platforms. Used by default on
  the web platform. This renderer uses OpenGL as the rendering driver.

Renderers, rendering drivers, and RenderingDevice

The renderer, or rendering method, determines which features are available.
Most of the time, this is the only thing you need to think about. Godot's renderers
are Forward+, Mobile, and Compatibility.

The rendering driver tells the GPU what to do, using a graphics API. Godot can
use the OpenGL, Vulkan, Direct3D 12, and Metal rendering drivers.
Not every GPU supports every rendering driver, and therefore not every GPU supports
all renderers. Vulkan, Direct3D 12, and Metal are modern, low-level graphics APIs,
and require newer hardware. OpenGL is an older graphics API that runs on most hardware.

RenderingDevice is a rendering backend, an abstraction layer between the renderer
and the rendering driver. It is used by the Forward+ and Mobile renderers, and
these renderers are sometimes called "RenderingDevice-based renderers".

Choosing a renderer

Choosing a renderer is a complex question, and depends on your hardware and the
which platforms you are developing for. As a starting point:

Choose Forward+ if:

You are developing for desktop.
You have relatively new hardware which supports Vulkan, Direct3D 12, or Metal.
You are developing a 3D game.
You want to use the most advanced rendering features.

Choose Mobile if:

You are developing for newer mobile devices, desktop XR, standalone XR, or
      desktop.
You have relatively new hardware which supports Vulkan, Direct3D 12, or Metal.
You are developing a 3D game.
You want to use advanced rendering features, subject to the limitations
      of mobile hardware.

Choose Compatibility if:

You are developing for older mobile devices, or older desktop devices.
      The Compatibility renderer supports the widest range of hardware.
You are developing for web. In this case, Compatibility is the only choice.
You have older hardware which does not support Vulkan. In this case,
      Compatibility is the only choice.
You are developing a 2D game, or a 3D game which does not need advanced
      rendering features.
You want the best performance possible on all devices and don't need advanced
      rendering features.

Keep in mind every game is unique, and this is only a starting point. For example,
you might choose to use the Compatibility renderer even though you have the latest
GPU, so you can support the widest range of hardware. Or you might want to use the
Forward+ renderer for a 2D game, so you can use advanced features like compute shaders.

Switching between renderers

In the editor, you can always switch between renderers by clicking on the renderer
name in the upper-right corner of the editor.

Switching between renderers may require some manual tweaks to your scene, lighting,
and environment, since each renderer is different. In general, switching between
the Mobile and Forward+ renderers will require fewer adjustments than switching
between the Compatibility renderer and the Forward+ or Mobile renderers.

Since Godot 4.4, when using Forward+ or Mobile, if Vulkan is not supported, the
engine will fall back to Direct3D 12 and vice versa. If the attempted fallback
driver is not supported either, the engine will then fall back to Compatibility
when the RenderingDevice backend is not supported. This allows the project to run
anyway, but it may look different than the intended appearance due to the more
limited renderer. This behavior can be disabled in the project settings by unchecking
Rendering > Rendering Device > Fallback to OpenGL 3.

Feature comparison

This is not a complete list of the features of each renderer. If a feature is
not listed here, it is available in all renderers, though it may be much faster
on some renderers. For a list of all features in Godot, see doc_list_of_features.

Hardware with RenderingDevice support is hardware which can run Vulkan, Direct3D
12, or Metal.

Overall comparison

+---------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+=====================+==========================+==========================+==========================+
Required | Older or low-end. | Newer or high-end. | Newer or high-end.
hardware Requires Vulkan, Direct3D| Requires Vulkan, Direct3D
12, or Metal support. | 12, or Metal support.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ✔️ Yes. | ✔️ Yes.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ✔️ Yes, but slower than | ✔️ Yes, but slowest of
Compatibility. | all renderers.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ❌ No. | ❌ No.

+---------------------+--------------------------+--------------------------+--------------------------+
Target platforms| Mobile, low-end desktop, | Mobile, desktop. | Desktop.
 web.

+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ✔️ Yes. | ✔️ Yes.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes (low-end). | ✔️ Yes (high-end). | ⚠️ Supported, but poorly
                           optimized. Use Mobile or
                           Compatibility instead.
+---------------------+--------------------------+--------------------------+--------------------------+
 ⚠️ Supported, but not | ✔️ Yes. Recommended for | ⚠️ Supported, but poorly
 recommended. Use Mobile optimized. Use Mobile or
 instead. | headsets. | Compatibility instead.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ❌ No. | ❌ No.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ✔️ Yes, but | ✔️ Yes, but
                           Compatibility is usually
good enough for 2D. | good enough for 2D.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ✔️ Yes. | ✔️ Yes.
+---------------------+--------------------------+--------------------------+--------------------------+
Feature set | 2D and core 3D features. | Most rendering features. | All rendering features.
+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ✔️ Yes. | ✔️ Yes.

+---------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Yes. | ✔️ Yes. | ✔️ Yes.

+---------------------+--------------------------+--------------------------+--------------------------+
 ❌ No. | ⚠️ Yes, limited by | ✔️ Yes. All rendering
mobile hardware. | features are supported.
+---------------------+--------------------------+--------------------------+--------------------------+
 ⚠️ Some new rendering | ✔️ Most new rendering | ✔️ All new features are
 features are added to added to Forward+. As the
 Compatibility. Features | Mobile. Mobile usually | focus of new development,
 are added after Mobile Forward+ gets features
 and Forward+. | Forward+ does. | first.
+---------------------+--------------------------+--------------------------+--------------------------+
 Low base cost, but | Medium base cost, and | Highest base cost, and
 high scaling cost. | medium scaling cost. | low scaling cost.
+---------------------+--------------------------+--------------------------+--------------------------+
 OpenGL. | Vulkan, Direct3D 12, or | Vulkan, Direct3D 12, or
Metal. | Metal.
+---------------------+--------------------------+--------------------------+--------------------------+

Lights and shadows

See doc_lights_and_shadows for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+=========================+==========================+==========================+==========================+
 Forward single-pass. | Forward single-pass. | Clustered forward.
 Lights with shadows use
 a multi-pass approach and
 less accurate blending.
+-------------------------+--------------------------+--------------------------+--------------------------+
 8 per mesh. Can be | 8 per mesh, 256 per view.| 512 per cluster. Can be
 increased. increased.
+-------------------------+--------------------------+--------------------------+--------------------------+
 8 per mesh. Can be | 8 per mesh, 256 per view.| 512 per cluster. Can be
 increased. increased.
+-------------------------+--------------------------+--------------------------+--------------------------+
 8 8

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+

Global Illumination

See doc_introduction_to_global_illumination for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+=========================+==========================+==========================+==========================+
 ✔️ Supported, 2 per | ✔️ Supported, 8 per | ✔️ Supported, unlimited.
 mesh. | mesh.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ⚠️ Rendering of baked | ✔️ Supported. | ✔️ Supported.
 lightmaps is supported.
 Baking requires hardware
 with RenderingDevice
 support.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.
Indirect Lighting (SSIL)
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.

(SDFGI)
+-------------------------+--------------------------+--------------------------+--------------------------+

Environment and post-processing

See doc_environment_and_post_processing for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+=========================+==========================+==========================+==========================+
Fog (Depth and Height) | ✔️ Supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Supported. | ❌ Not supported. | ✔️ Supported.
Occlusion (SSAO)
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.
Indirect Lighting (SSIL)
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.

(SDFGI)
+-------------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+

Antialiasing

See doc_3d_antialiasing for more information.

+-------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+===================+==========================+==========================+==========================+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.
+-------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.
+-------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.
+-------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.
+-------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------+--------------------------+--------------------------+--------------------------+

StandardMaterial features

See doc_standard_material_3d for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+=========================+==========================+==========================+==========================+
 ❌ Not supported. | ❌ Not supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+

Shader features

See doc_shading_reference for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+=========================+==========================+==========================+==========================+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ✔️ Supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
Normal/Roughness buffer | ❌ Not supported. | ❌ Not supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ⚠️ Supported, but comes | ✔️ Supported.

penalty on older devices.
+-------------------------+--------------------------+--------------------------+--------------------------+

Other features

+-------------------------+--------------------------+--------------------------+--------------------------+
 Compatibility Forward+
+=========================+==========================+==========================+==========================+
 RGBA8. Low dynamic range,| RGB10A2. Medium dynamic | RGBA16F. High dynamic
 medium precision. | range, low precision. | range, good precision.

enabled.
+-------------------------+--------------------------+--------------------------+--------------------------+
 24-bit without reverse Z.| 24-bit with reverse Z. | 32-bit with reverse Z.
 Medium precision. | Medium precision. | Good precision.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.
+-------------------------+--------------------------+--------------------------+--------------------------+
 ❌ Not supported. | ✔️ Supported. | ✔️ Supported.

+-------------------------+--------------------------+--------------------------+--------------------------+
