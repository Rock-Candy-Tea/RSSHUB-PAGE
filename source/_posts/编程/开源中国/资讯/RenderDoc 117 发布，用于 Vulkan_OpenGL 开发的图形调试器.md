
---
title: 'RenderDoc 1.17 发布，用于 Vulkan_OpenGL 开发的图形调试器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7278'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7278'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RenderDoc 是一种基于帧捕获（frame-capture based）的图形调试器，目前可用于 Windows、Linux、Android、Stadia 和 Nintendo Switch 上的 Vulkan、D3D11、D3D12、OpenGL 和 OpenGL ES 开发。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RenderDoc 1.17 发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">主要亮点</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持新的 Vulkan 扩展<span> </span><code>VK_KHR_dynamic_rendering</code>，该扩展允许在命令记录时跨命令缓冲区记录动态渲染通道，而不需要预先创建渲染通道或帧缓冲区对象。</li> 
 <li>资源检查器现在有了一些排序选项，你可以按字母顺序（之前的默认值）、创建顺序（根据它们在应用程序中的原始创建）或最近查看的顺序进行排序。当按最近查看排序时，顶部的资源是在资源检查器中最近查看的，并将依次进行排序。</li> 
 <li>计算着色器调试现在可以通过分割工作组和线程 ID，或通过全局线程 ID 启动。</li> 
 <li>网格查看器现在允许你选择输入顶点数据的坐标轴，例如用 Z-up 代替 Y-up 或左/右手。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Python API 的变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>ReplayController.GetCBufferVariableContents</code>现在在管线和着色器之后接受一个<span> </span><code>ShaderStage</code><span> </span>参数，以允许在像 vulkan 这样的 API 上进行歧义处理。</li> 
 <li><code>D3D12RootSignatureRange.rootElement</code><span> </span>已被重命名为<span> </span><code>D3D12RootSignatureRange.rootSignatureIndex</code>，以便更清楚地表明这是指原始元素。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">功能/改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>UI：性能计数器查看器现在只显示与事件浏览器同步的可见事件。</li> 
 <li>UI：自定义可视化着色器现在可以访问选定的最小/最大范围。</li> 
 <li>UI：增加了将编辑过的着色器重置为原始状态的功能。</li> 
 <li>OpenGL：增加对 3D ASTC 压缩纹理的支持。</li> 
 <li>Vulkan：增加一个选项，将当前的 vulkan 管道状态和依赖关系导出到 fossilize 数据库。</li> 
 <li>Vulkan：增加对一些新扩展的支持： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>VK_KHR_dynamic_rendering</li> 
   <li>VK_KHR_format_feature_flags2</li> 
   <li>VK_KHR_maintenance4</li> 
   <li>VK_KHR_present_id</li> 
   <li>VK_KHR_present_wait</li> 
   <li>VK_KHR_shader_integer_dot_product</li> 
   <li>VK_KHR_shader_subgroup_uniform_control_flow</li> 
   <li>VK_EXT_color_write_enable</li> 
   <li>VK_EXT_extended_dynamic_state2</li> 
   <li>VK_EXT_fragment_density_map2</li> 
   <li>VK_EXT_global_priority_query</li> 
   <li>VK_EXT_load_store_op_none</li> 
   <li>VK_EXT_rgba10x6_formats</li> 
   <li>VK_EXT_shader_atomic_float2</li> 
   <li>VK_EXT_vertex_input_dynamic_state</li> 
   <li>VK_EXT_ycbcr_2plane_444_formats</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaldurk%2Frenderdoc%2Freleases%2Ftag%2Fv1.17" target="_blank">https://github.com/baldurk/renderdoc/releases/tag/v1.17</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            