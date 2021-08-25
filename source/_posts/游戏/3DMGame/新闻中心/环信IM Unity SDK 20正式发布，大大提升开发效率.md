
---
title: '环信IM Unity SDK 2.0正式发布，大大提升开发效率'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210825/1629859661_374736.jpg'
author: 3DMGame
comments: false
date: Wed, 25 Aug 2021 02:48:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210825/1629859661_374736.jpg'
---

<div>   
<p style="text-indent:2em;">
引言
</p>
<p style="text-indent:2em;">
Untiy作为游戏引擎和内容开发平台，吸引了众多游戏开发者，基于其开发的游戏更是不胜其数。具体请参见1。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629859661_374736.jpg" alt="环信IM Unity SDK 2.0正式发布，大大提升开发效率" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
环信作为领先的即时通讯云服务商，在游戏行业也进行了持续的探索和研发投入。在产品发布的早期(2015年)就推出了Unity 
SDK，帮助游戏开发者快速实现游戏场景下诸如世界频道，游戏公会、组队群聊，1对1私聊等功能，安全稳定的服务也为游戏玩家带来了极佳的实时沟通体验。
</p>
<p style="text-indent:2em;">
2021年第二季度，环信IM Unity SDK进行了重构改版，环信IM Unity SDK 2.0正式发布，主要改进包括如下：
</p>
<p style="text-indent:2em;">
1、迭代更新，更加实用的API接口
</p>
<p style="text-indent:2em;">
2、IM+Push增强功能的补全
</p>
<p style="text-indent:2em;">
3、C#语言层面引入了版本7.0 – 9.0之后的一些新语法改进
</p>
<p style="text-indent:2em;">
4、特别的，增加了PC端Unity Editor环境下编译调试支持，大大提升了开发效率
</p>
<p style="text-indent:2em;">
在过去的一段时间里，笔者也参与了相应的研发工作。在整个过程中，为了解决各种问题，不仅要到处翻阅资料，还要尝试各种方法和参数组合。其间也经历了各种程序崩溃甚至系统崩溃，诡异的程序表现一次次让开发人员束手无策，四处碰壁，当真像深夜里行走在迷宫之中，手里还拿着一个待破解的魔方。“此路不通，请绕行!”，是在一次次的尝试后无奈的慨叹和难舍的放弃。而一旦问题最后得到圆满解决，又宛如飞入云端，以上帝视角俯瞰一片片迷宫，一切又显得那么理所当然，繁复琐细但又丝丝入扣，这样的苦尽甘来也算是做程序员能享受到的巨大喜悦和满足。
</p>
<p style="text-indent:2em;">
不敢独享，特记录下一些心得供大家参考，也欢迎.NET平台资深玩家批评指正。以下，Enjoy!
</p>
<p style="text-indent:2em;">
开发概览：非托管插件开发(Native/Unmanaged Plugin)
</p>
<p style="text-indent:2em;">
Unity是基于Microsoft .Net Framework开发的游戏引擎2，它采用了开源的.NET 
Platform，并依赖此框架来实现跨硬件设备和运行时(操作系统)的目标，也是所谓的”Write once, run 
anywhere”。在语言方面，Unity选择C#作为主要的脚本编程语言，虽然.NET平台本身支持的语言有很多种。
</p>
<p style="text-indent:2em;">
进一步，Unity支持Mono和ILC2PP两种脚本框架(Scripting Backends)。特别的，Unity 
Editor采用的是Mono脚本框架。
</p>
<p style="text-indent:2em;">
一般的，游戏类库开发者可以选择直接用C#语言开发，目标类库可以实现基于.NET Framework基础功能之上的高级功能，这类插件称之为Managed 
Plugin(托管插件)。由于环信IM核心SDK已经基于C++开发，因此我们选择另一种Native 
Plugin(本地插件)的方式，正是它把我们引向了迷宫之旅。两种类型的Plugin介绍，参见3。
</p>
<p style="text-indent:2em;">
不幸的是，Unity网站上关于Native Plugin的相关介绍少只又少，想要了解它的具体细节还要去参考Microsoft 
MSDN文档。作为中规中矩的文档介绍，微软的文档是合格的，但是，当你真正上手编程时就会发现，这些远远不够：下面记录的一些坑点就很难在相应的文档中得到直接的提示;而要通过Google大法，结合其他程序员留下的蛛丝马迹，再加上自己不断的调试来最终确认。
</p>
<p style="text-indent:2em;">
在微软文档上下文中，Unity Native Plugin有个另外的名字：Unmanaged Plugin，即非托管插件。简单来讲，Managed 
Plugin生存在.NET Framework的运行时环境(类似于Java的JVM)，而Unmanaged 
Plugin则生存在这个运行时环境之外，也即和运行时环境是兄弟的关系。如果你原本的类库实现满足微软的COM(Component Object 
Model)规范，那自然最好是使用COM Interop4的互操作方式;而环信IM SDK本身是纯C++实现，因此采用了Platform 
Invoke5(简称P/Invoke)方式，本文剩下的内容均是基于P/Invoke。
</p>
<p style="text-indent:2em;">
下图则概要描述了Managed和Unmanaged区域代码之间互相操作的方式：
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629859661_402498.gif" alt="环信IM Unity SDK 2.0正式发布，大大提升开发效率" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
更具体的，为了实现对于Unmanaged DLL function的调用，只需要简单的4步6：
</p>
<p style="text-indent:2em;">
1、确认DLL类库中需要被操作的函数;
</p>
<p style="text-indent:2em;">
2、创建一个C#类来关联被操作的这些函数(给函数穿上一个马甲，以便集中管理和反复调用);
</p>
<p style="text-indent:2em;">
3、使用DllImport标志在受管侧(C#)定义函数原型;
</p>
<p style="text-indent:2em;">
4、在受管侧随意调用相关非托管区域函数。
</p>
<p style="text-indent:2em;">
上图中，Standard marshalling 
service即负责将数据在两个区域进行封装/解封装传送(marshall/unmarshall)，它主要定义了数据在两个不同内存区域进行拷贝(Copy)和引用(Reference)的规则7，而迷宫中的坑主要是和这些具体规则有关。
</p>
<p style="text-indent:2em;">
坑王驾到之封送(Marshall/Unmarshall)中的那些坑
</p>
<p style="text-indent:2em;">
<strong>坑一：sizeof(bool) = ?</strong>
</p>
<p style="text-indent:2em;">
绝大多数的基本类型属于Blittable Types8：如System.Byte, 
System.Single等。System.Boolean虽然不属于Blittable types，但是Standard Marshalling 
Service默认将其转换为1,2,4字节的内存存储，当其值为true时，其对应的值为1。如果你想当然的直接将System.Boolean映射到Unmanaged侧的bool类型而不做特别处理的话，你并一定会理解碰到编译或者运行时错误，但是如果你严格的测试每个字段是，会惊讶的发现这些bool值跟你想象的不尽相同：有时正确，有时错误。
</p>
<p style="text-indent:2em;">
经过调试跟踪，动态打印sizeof(bool)来确认Unmanaged侧bool类型数据长度后，你会发现System.Boolean默认会被保存为4个字节长度，而在macOS环境下(对于其它环境，需要自行认证)，C++定义的bool其实只有一个字节。因此当你在Unmanaged侧取bool值的时候，其实只读取了System.Boolean的1/4个字节而已。而当你声明了多个连续的System.Boolean/bool值时，可能在Unmanaged侧读取的这几个bool值仅仅是第一个System.Boolean值的不同偏移字节而已。
</p>
<p style="text-indent:2em;">
知道了原因，解决方案自然就出来了，在Managed侧强制声明System.Boolean字段封送到Unmanaged侧时仅使用一个字节：
</p>
<p style="text-indent:2em;">
[MarshallAs(UnmanagedType.U1)]public bool TrueOrFalse;
</p>
<p style="text-indent:2em;">
<strong>坑二：字节对齐</strong>
</p>
<p style="text-indent:2em;">
对于C++开发者来说，可能知道当一个数据结构(class or 
struct)中的各字段在内存中进行排列时，会按照一个设定的装箱长度进行字节对齐，例如：
</p>
<p style="text-indent:2em;">
struct MyStruct &#123;
</p>
<p style="text-indent:2em;">
int one;
</p>
<p style="text-indent:2em;">
short two;
</p>
<p style="text-indent:2em;">
int three;
</p>
<p style="text-indent:2em;">
bool four;
</p>
<p style="text-indent:2em;">
&#125;
</p>
<p style="text-indent:2em;">
假设在我们的平台上，sizeof(int)=4, sizeof(short)=2, sizeof(bool)=1, 
如果问你sizeof(MyStruct)=?，你可能会马上做个加法得到答案，但是答案不一定对。It depends! 
假设我们是按照4个字节对齐，这上面的结构体在内存中实际排列如下图：
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210825/1629859661_195218.png" alt="环信IM Unity SDK 2.0正式发布，大大提升开发效率" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
了解这个对于我们编码有两个意义：
</p>
<p style="text-indent:2em;">
1、通过合理排列字段声明顺序来优化存储效率，内存布局中不留空洞;
</p>
<p style="text-indent:2em;">
2、MarshalAsAttribute支持Layout.Explicit来进行绝对定位，懂得了字节对齐可以配合Unmanaged侧的内存排列规则以保证字段长度映射正确，不然同样会发生字段长度不一致带来的困扰。
</p>
<p style="text-indent:2em;">
<strong>坑三：如何避免Double Free</strong>
</p>
<p style="text-indent:2em;">
Standard Marshalling Service/Interop 
marshaller总是试图释放Unmanaged侧代码分配的内存9，这会带来Double Free的问题，如果碰到这种问题，程序就会直接崩溃。
</p>
<p style="text-indent:2em;">
引用资料中举了以下例子：
</p>
<p style="text-indent:2em;">
BSTR MethodOne (BSTR b) &#123;
</p>
<p style="text-indent:2em;">
return b;
</p>
<p style="text-indent:2em;">
&#125;
</p>
<p style="text-indent:2em;">
如果这段代码直接从Unmanaged侧DLL中直接执行，不会发生任何额外的内存释放;但是当你从Managed侧调用这个方法时，b会被释放两次。
</p>
<p style="text-indent:2em;">
而更让人抓狂的是，并没有相应的信息提示究竟是哪个指针，哪个字段被Double 
Free了，你唯一能做的就是一点点加代码来验证自己猜测。所以，严格来说，并没有一个万无一失的方案来避免Double 
Free，你唯一能做的就是通过测试来验证结果(有点盲拧魔方的味道了)。
</p>
<p style="text-indent:2em;">
有两个基本的方法来解决Double Free的问题：
</p>
<p style="text-indent:2em;">
1、按照官方文档建议，在Unmanaged侧通过使用CoTaskMemAlloc来分配内存，通过此种方法分配的内存，除非显式调用了CoTaskMemFree方法(在Unmanaged侧或者Managed侧均可以调用)，Interop 
Marshaller会严格保证不去释放该内存。使用这种方法可以灵活的在任意一侧分配内存，并在合适的时候在另一侧释放内存。
</p>
<p style="text-indent:2em;">
2、但上面这种方法貌似仅适用于Windows平台，在macOS下没有办法使用(需要引用win32base.dll相关实现)。在macOS下仅能通过在Mananged侧调用Marshal.AllocCoTaskMem()方法分配内存，并通过Marshal.FreeCoTaskMem()来在同一侧进行释放(按照此方法分配的内存指针传入Unmanaged侧后，不要进行任何释放即可)。另外有一个不太可靠的workaround是：在Unmanaged一侧创建的内存指针尽量通过IntPtr传递，并在可能的时候将对象中一些指针类型的属性值置空，以避免Double 
Free的发生。
</p>
<p style="text-indent:2em;">
<strong>坑四：virtual函数带来的内存布局变化</strong>
</p>
<p style="text-indent:2em;">
vptr和vtable是C++的一个概念：当你定义的类型中有虚函数存在时，内存对象的第一个位置会存放一个vptr指针，该指针指向vtable(虚函数表)。因此当你开始创建的自定义类型一开始没有虚函数时(包括虚析构函数virtual 
~MyClass())，一切运行正常。有一天你重构此类型，增加了一些虚函数：DUANG，一切都崩塌了!原因就在于Unmanaged侧内存对象的排列规则变了，原有的对象字段都被新加入的vptr往后面移位了。此时可能你唯一能做的就是通过Layout.Explicit来手工对齐每一个字段新的位置。
</p>
<p style="text-indent:2em;">
<strong>其它坑</strong>
</p>
<p style="text-indent:2em;">
坑一：针对M1芯片编译
</p>
<p style="text-indent:2em;">
对于M1芯片的macOS系统，编译环信IM Unity SDK时候需要注意几个问题：
</p>
<p style="text-indent:2em;">
1、XCode编译时需要Excluded Architecture中排除arm64架构(很奇葩的设置，不是应该排除x86吗?)
</p>
<p style="text-indent:2em;">
2、类库的依赖解决：通过otool 
-L命令来确认相应的plugin依赖的类库位置都正确(文件路径下文件确实存在)，如果相应文件不存在要手工拷贝文件到指定目录：而新的macOS安全架构限制了往系统目录下(如/usr/lib)进行任何改动，一个临时的解决方法是通过install_name_tool工具主动修改类库依赖路径到另一个可以放置新文件的位置(如home目录)。
</p>
<p style="text-indent:2em;">
坑二：Delegate的正确使用姿势
</p>
<p style="text-indent:2em;">
如果Managed侧的编程语言是C#，则Delegate是实现回调的重要手段。在Unmanaged侧完成期望工作时回调一个FunctionPtr即可实现通用的回调模式，而此FunctionPtr正是对应到Managed侧的Delegate。当你的Delegate绑定到一个类对象上时，你有两种选择：
</p>
<p style="text-indent:2em;">
namespace ChatSDK &#123;
</p>
<p style="text-indent:2em;">
//delegate definition
</p>
<p style="text-indent:2em;">
public void delegate OnMessageReceived(EMMessage message);
</p>
<p style="text-indent:2em;">
public class MyDelegate &#123;
</p>
<p style="text-indent:2em;">
//Option 1: field
</p>
<p style="text-indent:2em;">
public OnMessageReceived MyMessageReceived;
</p>
<p style="text-indent:2em;">
//Option 2: instance method
</p>
<p style="text-indent:2em;">
public void OnMessageReceived(EMMessage message)
</p>
<p style="text-indent:2em;">
&#123;
</p>
<p style="text-indent:2em;">
...
</p>
<p style="text-indent:2em;">
&#125;
</p>
<p style="text-indent:2em;">
&#125;
</p>
<p style="text-indent:2em;">
//send delegate method to unmanaged side
</p>
<p style="text-indent:2em;">
MyDelegate md = new();
</p>
<p style="text-indent:2em;">
NativeMethods.SetOnMessageReceivedCallback(md.MyMessageReceived); //option 
1
</p>
<p style="text-indent:2em;">
NativeMethods.SetOnMessageReceivedCallback(md.OnMessageReceived); //option 
2
</p>
<p style="text-indent:2em;">
&#125;
</p>
<p style="text-indent:2em;">
看起来两个方式都没有问题，并且第二个方式看起来更顺眼。但是这里隐藏着一个很深的坑，就是你选择第二个方式的时候，如果你在回调方法实现中采用this.xxx方式引用时，你会发现this 
= 
null!这是因为当你使用这种方式传递一个对象的方法作为回调方法指针时，其实已经丢失了Delegate.Target(也就是this)属性。而通过第一种方式传递的是一个对象的属性/字段，它和对象本身的绑定是不会在传递过程中丢失的。
</p>
<p style="text-indent:2em;">
至于该Delegate字段的定义可以在此类的构造函数中通过以下方式实现：
</p>
<p style="text-indent:2em;">
...
</p>
<p style="text-indent:2em;">
public MyDelegate() &#123;
</p>
<p style="text-indent:2em;">
MyMessageReceived = (EMMessage message) => &#123; ... &#125;
</p>
<p style="text-indent:2em;">
&#125;
</p>
<p style="text-indent:2em;">
...
</p>          
</div>
            