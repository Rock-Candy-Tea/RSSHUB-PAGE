
---
title: 'Taichi v0.8.0 发布，带来更流畅的 GUI 体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b8ac40d8db1b188ece99d3d03231d07b4fc.png'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 07:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b8ac40d8db1b188ece99d3d03231d07b4fc.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-b8ac40d8db1b188ece99d3d03231d07b4fc.png" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">​9月23日，太极图形团队发布了<u><em><strong>Taichi v0.8.0</strong></em></u>，此版本公布了一个新的 Vulkan 后端，以及一套基于 Vulkan 的 GUI API (GGUI)。同时，此版本还包括一些重要的改进，比如紧凑排布模式和动态SNode申请。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">紧凑排布模式（Packed Mode）</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">此前，Taichi field所有维度上的尺寸都会被自动扩展到 2 的幂。例如，用户定义尺寸为<span> </span><code>(18, 65)</code>的 field 实际内部尺寸为<code>(32, 128)</code>。尽管扩展到 2 的幂有许多好处，如允许在坐标处理时使用快速方便的位运算，但它往往会消耗更多的内存。为了满足人们对更小内存占用的需求，Taichi 引入了一个可选的紧凑排布模式。在这种模式下不会进行尺寸的自动扩展，因此当field某些维度的尺寸不是2的幂时不会再占用更多的内存。这样当然也有一定的缺点，即程序的运行性能会有轻微的下降。紧凑排布模式可通过在<code>ti.init()</code>里设置<code>packed=True</code>开启。</p> 
<pre><code># default: packed=False
ti.init()
# padded to (32, 128)
a = ti.field(ti.i32, shape=(18, 65))</code></pre> 
<pre><code>ti.init(packed=True)
# no padding
a = ti.field(ti.i32, shape=(18, 65))</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:start">GPU上的图形使用者界面（GGUI）</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Taichi 中增加了一个新的GUI 系统，代号为 GGUI。GGUI将使用Vulkan进行渲染，这使得它比之前的<code>ti.gui</code>快很多，并且可以用于渲染 3D 网格和粒子。同时，它还带有一组全新的绘制UI的API。这组API底层基于imgui，采用即时模式（immediate mode）进行控件渲染。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0929/072107_bJcg_2720166.png" referrerpolicy="no-referrer"></p> 
<p>3D代码示例</p> 
<pre><code>window = ti.ui.Window("Hello Taichi", (1920, 1080))

canvas = window.get_canvas()
scene = ti.ui.Scene()
camera = ti.ui.make_camera()

while window.running:

    camera.position(...)
    camera.lookat(...)
    scene.set_camera(camera)

    scene.point_light(pos=(...), color=(...))

    # vertices, centers, etc. are taichi fields
    scene.mesh(vertices, ...)
    scene.particles(centers, radius, ...)

    canvas.scene(scene)
    window.show()</code></pre> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">IMGUI代码示例</p> 
<pre><code>window = ti.ui.Window("Hello Taichi", (500, 500))
canvas = window.get_canvas()

gx, gy, gz = (0, -9.8, 0)

while window.running:

    window.GUI.begin("Greetings", 0.1, 0.1, 0.8, 0.15)
    window.GUI.text("Welcome to TaichiCon !")
    if window.GUI.button("Bye"):
        window.running = False
    window.GUI.end()

    window.GUI.begin("Gravity", 0.1, 0.3, 0.8, 0.3)
    gx = window.GUI.slider_float("x", gx, -10, 10)
    gy = window.GUI.slider_float("y", gy, -10, 10)
    gz = window.GUI.slider_float("z", gz, -10, 10)
    window.GUI.end()

    canvas.set_background_color(color)
    window.show()</code></pre> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">目前支持 GGUI 的平台包括 Linux 和 Windows 10。在使用之前请先安装 Vulkan。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">更多示例，可以在 taichi repo里搜索<span> </span><code>examples/ggui_examples</code></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">动态SNode申请（Dynamic SNode Allocation）</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">此前版本的 Taichi 中，一个限制是所有 fields 必须在执行第一个 Taichi kernel 之前被定义。随着 v0.8.0 的到来，你可以借助其中一个重要的新功能——<span> </span><code>FieldsBuilder</code>类，来实现 fields 的动态申请。<code>FieldsBuilder</code>在声明 SNode 数据结构时所使用的接口，与之前<code>ti.root</code>的接口保持一致。诸如<code>dense()</code><span> </span>、<code>pointer()</code><span> </span>等大家常用的接口在<code>FieldsBuilder</code>中是依然支持的。在声明完 SNode 数据结构的排布后，你需要调用<code>finalize()</code>函数将<span> </span><code>FieldsBuilder</code>里添加的 fields 进行实例化编译，并得到一个<code>SNodeTree</code>对象。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><code>FieldsBuilder</code>代码示例：</p> 
<pre><code>import taichi as ti
ti.init()

@ti.kernel
def func(v: ti.template()):
    for I in ti.grouped(v):
        v[I] += 1

fb = ti.FieldsBuilder()
x = ti.field(dtype = ti.f32)
fb.dense(ti.ij, (5, 5)).place(x)
# Finalizing the FieldsBuilder and returns a SNodeTree
fb_snode_tree = fb.finalize()
func(x)

fb2 = ti.FieldsBuilder()
y = ti.field(dtype = ti.f32)
fb2.dense(ti.i, 5).place(y)
# Finalizing the FieldsBuilder and returns a SNodeTree
fb2_snode_tree = fb2.finalize()
func(y)</code></pre> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">此外，Taichi v0.8.0 使用<code>FieldsBuilder</code>重新实现了<code>ti.root</code><span> </span>。每当一个 Taichi kernel 被调用时，如果<code>ti.root</code>上目前有尚未实例化的 fields ，Taichi 会先将其自动实例化编译为新的<code>SNodeTree</code>对象，并创建一个新的<code>FieldsBuilder</code>，供<code>ti.root</code>继续添加更多 fields。</p> 
<pre><code>import taichi as ti
# ti.root = ti.FieldsBuilder()
ti.init()
@ti.kernel
def func(v: ti.template()):
    for I in ti.grouped(v):
        v[I] += 1

x = ti.field(dtype = ti.f32)
ti.root.dense(ti.ij, (5, 5)).place(x)
# automatically called ti.root.finalize()
# ti.root = new ti.FieldsBuilder()
func(x)

y = ti.field(dtype = ti.f32)
ti.root.dense(ti.i, 5).place(y)
# automatically called ti.root.finalize()
func(y)</code></pre> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">当我们不再需要使用某个<code>SNodeTree</code>中包含的fields时，我们可以手动调用<code>destroy()</code>函数，摧毁这个<code>SNodeTree</code>对象，其内存会被回收以供新的<code>SNodeTree</code>使用。</p> 
<pre><code>import taichi as ti
ti.init()

@ti.kernel
def func(v: ti.template()):
    for I in ti.grouped(v):
        v[I] += 1

fb = ti.FieldsBuilder()
x = ti.field(dtype = ti.f32)
fb.dense(ti.ij, (5, 5)).place(x)
# Finalizing the FieldsBuilder and returns a SNodeTree
fb_snode_tree = fb.finalize()
func(x)

# func(x) cannot be used anymore
fb_snode_tree.destroy()</code></pre> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">目前支持该功能的后端包括CPU, CUDA和Vulkan。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">前往<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2974" target="_blank">GitHub主页</a>可查看完整的发布信息。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">原文地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F414262807" target="_blank">https://zhuanlan.zhihu.com/p/414262807</a></p>
                                        </div>
                                      
</div>
            