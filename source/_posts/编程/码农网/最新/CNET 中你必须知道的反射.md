
---
title: 'C#.NET 中你必须知道的反射'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://picsum.photos/400/300?random=651'
author: 码农网
comments: false
date: Wed, 10 Jun 2020 08:13:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=651'
---

<div>   
<p>通常，反射用于动态获取对象的类型、属性和方法等信息。今天带你玩转反射，来汇总一下反射的各种常见操作，捡漏看看有没有你不知道的。</p>
<h2 id="获取类型的成员">获取类型的成员</h2>
<p>Type 类的 GetMembers 方法用来获取该类型的所有成员，包括方法和属性，可通过 BindingFlags 标志来筛选这些成员。</p>
<pre class="brush: csharp; gutter: true; first-line: 1">using System;
using System.Reflection;
using System.Linq;

public class Program
&#123;
    public static voidMain()
    &#123;
        var members = typeof(object).GetMembers(BindingFlags.Public |
            BindingFlags.Static | BindingFlags.Instance);
        foreach (var member in members)
        &#123;
            Console.WriteLine($"&#123;member.Name&#125; is a &#123;member.MemberType&#125;");
        &#125;
    &#125;
&#125;</pre>
<p>输出：</p>
<pre class="brush: csharp; gutter: true; first-line: 1; html-script: true">GetType is a Method
GetHashCode is a Method
ToString is a Method
Equals is a Method
ReferenceEquals is a Method
.ctor is a Constructor</pre>
<p>GetMembers 方法也可以不传 BindingFlags，默认返回的是所有公开的成员。</p>
<h2 id="获取并调用对象的方法">获取并调用对象的方法</h2>
<p>Type 类型的 GetMethod 方法用来获取该类型的 MethodInfo，然后可通过 MethodInfo 动态调用该方法。</p>
<p>对于非静态方法，需要传递对应的实例作为参数，示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">class Program
&#123;
    public static void Main()
    &#123;
        var str = "hello";
        var method = str.GetType()
            .GetMethod("Substring", new[] &#123;typeof(int), typeof(int)&#125;);
        var result = method.Invoke(str, new object[] &#123;0, 4&#125;); // 相当于 str.Substring(0, 4)
        Console.WriteLine(result); // 输出：hell
    &#125;
&#125;</pre>
<p>对于静态方法，则对象参数传空，示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">var method = typeof(Math).GetMethod("Exp");
// 相当于 Math.Exp(2)
var result = method.Invoke(null, new object[] &#123;2&#125;);
Console.WriteLine(result); // 输出(e^2)：7.38905609893065</pre>
<p>如果是泛型方法，则还需要通过泛型参数来创建泛型方法，示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">class Program
&#123;
    public static void Main()
    &#123;
        // 反射调用泛型方法
        MethodInfo method1 = typeof(Sample).GetMethod("GenericMethod");
        MethodInfo generic1 = method1.MakeGenericMethod(typeof(string));
        generic1.Invoke(sample, null);

        // 反射调用静态泛型方法
        MethodInfo method2 = typeof(Sample).GetMethod("StaticMethod");
        MethodInfo generic2 = method2.MakeGenericMethod(typeof(string));
        generic2.Invoke(null, null);
    &#125;
&#125;

public class Sample
&#123;
    public void GenericMethod<T>()
    &#123;
        //...
    &#125;
    public static void StaticMethod<T>()
    &#123;
        //...
    &#125;
&#125;</pre>
<h2 id="创建一个类型的实例">创建一个类型的实例</h2>
<p>使用反射动态创建一个类型的实例有多种种方式。最简单的一种是用 <code>new()</code> 条件声明。</p>
<h3 id="使用-new-条件声明">使用 new 条件声明</h3>
<p>如果在一个方法内需要动态创建一个实例，可以直接使用 new 条件声明，例如：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">T GetInstance<T>() where T : new()
&#123;
    T instance = newT();
    return instance;
&#125;</pre>
<p>但这种方式适用场景有限，比如不适用于构造函数带参数的类型。</p>
<h3 id="使用-activator-类">使用 Activator 类</h3>
<p>使用 Activator 类动态创建一个类的实例是最常见的做法，示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">Type type = typeof(BigInteger);
object result = Activator.CreateInstance(type);
Console.WriteLine(result); // 输出：0
result = Activator.CreateInstance(type, 123);
Console.WriteLine(result); // 输出：123</pre>
<p>动态创建泛类型实例，需要先创建开放泛型（如<code>List<></code>），再根据泛型参数转换为具象泛型（如<code>List<string></code>），示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">// 先创建开放泛型
Type openType = typeof(List<>);
// 再创建具象泛型
Type[] tArgs = &#123; typeof(string) &#125;;
Type target = openType.MakeGenericType(tArgs);
// 最后创建泛型实例
List<string> result = (List<string>)Activator.CreateInstance(target);</pre>
<p>如果你不知道什么是开放泛型和具象泛型，请看本文最后一节。</p>
<h3 id="使用构造器反射">使用构造器反射</h3>
<p>也可以通过反射构造器的方式动态创建类的实例，比上面使用 Activator 类要稍稍麻烦些，但性能要好些。示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">ConstructorInfo c = typeof(T).GetConstructor(new[] &#123; typeof(string) &#125;);
if (c == null)
    throw new InvalidOperationException("...");
T instance = (T)c.Invoke(new object[] &#123; "test" &#125;);</pre>
<h3 id="使用-formatterservices-类">使用 FormatterServices 类</h3>
<p>如果你想创建某个类的实例的时候不执行构造函数和属性初始化，可以使用 FormatterServices 的 GetUninitializedObject 方法。示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">class Program
&#123;
    static void Main()
    &#123;
        MyClass instance = (MyClass)FormatterServices.GetUninitializedObject(typeof(MyClass));
        Console.WriteLine(instance.MyProperty1); // 输出：0
        Console.WriteLine(instance.MyProperty2); // 输出：0
    &#125;
&#125;

public class MyClass
&#123;
    public MyClass(int val)
    &#123;
        MyProperty1 = val < 1 ? 1 : val;
    &#125;

    public int MyProperty1 &#123; get; &#125;

    public int MyProperty2 &#123; get; set; &#125; = 2;
&#125;</pre>
<h2 id="获取属性或方法的强类型委托">获取属性或方法的强类型委托</h2>
<p>通过反射获取到对象的属性和方法后，如果你想通过强类型的方法来访问或调用，可以在中间加一层委托。这样的好处是有利于封装，调用者可以明确的知道调用时需要传什么参数。 比如下面这个方法，把 Math.Max 方法提取为一个强类型委托：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">var tArgs = new Type[] &#123; typeof(int), typeof(int) &#125;;
var maxMethod = typeof(Math).GetMethod("Max", tArgs);
var strongTypeDelegate = (Func<int, int, int>)Delegate
    .CreateDelegate(typeof(Func<int, int, int>), null, maxMethod);
Console.WriteLine("3 和 5 之间最大的是：&#123;0&#125;", strongTypeDelegate(3, 5)); // 输出：5</pre>
<p>这个技巧也适用于属性，可以获取强类型的 Getter 和 Setter。示例：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">var theProperty = typeof(MyClass).GetProperty("MyIntProperty");

// 强类型 Getter
var theGetter = theProperty.GetGetMethod();
var strongTypeGetter = (Func<MyClass, int>)Delegate
    .CreateDelegate(typeof(Func<MyClass, int>), theGetter);
var intVal = strongTypeGetter(target); // 相关于：target.MyIntProperty

// 强类型 Setter
var theSetter = theProperty.GetSetMethod();
var strongTypeSetter = (Action<MyClass, int>)Delegate
    .CreateDelegate(typeof(Action<MyClass, int>), theSetter);
strongTypeSetter(target, 5); // 相当于：target.MyIntProperty = 5</pre>
<h2 id="反射获取自定义特性">反射获取自定义特性</h2>
<p>以下是四个常见的场景示例。</p>
<p><strong>示例一，</strong>找出一个类中标注了某个自定义特性（比如 MyAtrribute）的属性。</p>
<pre class="brush: csharp; gutter: true; first-line: 1">var props = type
    .GetProperties(BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Instance)
    .Where(prop =>Attribute.IsDefined(prop, typeof(MyAttribute)));</pre>
<p><strong>示例二，</strong>找出某个属性的所有自定义特性。</p>
<pre class="brush: csharp; gutter: true; first-line: 1">var attributes = typeof(t).GetProperty("Name").GetCustomAttributes(false);</pre>
<p><strong>示例三，</strong>找出程序集所有标注了某个自定义特性的类。</p>
<pre class="brush: csharp; gutter: true; first-line: 1">static IEnumerable<Type> GetTypesWithAttribute(Assembly assembly)
&#123;
    foreach(Type type inassembly.GetTypes())
    &#123;
        if (type.GetCustomAttributes(typeof(MyAttribute), true).Length > 0)
        &#123;
            yield return type;
        &#125;
    &#125;
&#125;</pre>
<p><strong>示例四，</strong>在运行时读取自定义特性的值</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public static class AttributeExtensions
&#123;
    public static TValue GetAttribute<TAttribute, TValue>(
        this Type type,
        string MemberName,
        Func<TAttribute, TValue> valueSelector,
        bool inherit = false)
        where TAttribute : Attribute
    &#123;
        var att = type.GetMember(MemberName).FirstOrDefault()
            .GetCustomAttributes(typeof(TAttribute), inherit)
            .FirstOrDefault() as TAttribute;
        if (att != null)
        &#123;
            return valueSelector(att);
        &#125;
        return default;
    &#125;
&#125;

// 使用：

class Program
&#123;
    static void Main()
    &#123;
        // 读取 MyClass 类的 MyMethod 方法的 Description 特性的值
        var description = typeof(MyClass)
            .GetAttribute("MyMethod", (DescriptionAttribute d) => d.Description);
        Console.WriteLine(description); // 输出：Hello
    &#125;
&#125;
public class MyClass
&#123;
    [Description("Hello")]
    public void MyMethod() &#123; &#125;
&#125;</pre>
<h2 id="动态实例化接口的所有实现类（插件激活）">动态实例化接口的所有实现类（插件激活）</h2>
<p>通过反射来动态实例化某个接口的所有实现类，常用于实现系统的插件式开发。比如在程序启动的时候去读取指定文件夹（如 Plugins）中的 dll 文件，通过反射获取 dll 中所有实现了某个接口的类，并在适当的时候将其实例化。大致实现如下：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">interface IPlugin
&#123;
    string Description &#123; get; &#125;
    void DoWork();
&#125;</pre>
<p>某个在独立 dll 中的类：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">class HelloPlugin : IPlugin
&#123;
    public string Description => "A plugin that says Hello";
    public void DoWork()
    &#123;
        Console.WriteLine("Hello");
    &#125;
&#125;</pre>
<p>在你的系统启动的时候动态加载该 dll，读取实现了 IPlugin 接口的所有类的信息，并将其实例化。</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public IEnumerable<IPlugin> InstantiatePlugins(string directory)
&#123;
    var assemblyNames = Directory.GetFiles(directory, "*.addin.dll")
        .Select(name => new FileInfo(name).FullName).ToArray();

    foreach (var fileName assemblyNames)
        AppDomain.CurrentDomain.Load(File.ReadAllBytes(fileName));

    var assemblies = assemblyNames.Select(System.Reflection.Assembly.LoadFile);
    var typesInAssembly = assemblies.SelectMany(asm =>asm.GetTypes());
    var pluginTypes = typesInAssembly.Where(type => typeof (IPlugin).IsAssignableFrom(type));

    return pluginTypes.Select(Activator.CreateInstance).Cast<IPlugin>();
&#125;</pre>
<h2 id="检查泛型实例的泛型参数">检查泛型实例的泛型参数</h2>
<p>前文提到了构造泛型和具象泛型，这里解释一下。大多时候我们所说的泛型都是指<strong>构造泛型</strong>，有时候也被称为<strong>具象泛型</strong>。比如 <code>List<int></code> 就是一个构造泛型，因为它可以通过 new 来实例化。相应的，<code>List<></code>泛型是<strong>非构造泛型</strong>，有时候也被称为<strong>开放泛型</strong>，它不能被实例化。开放泛型通过反射可以转换为任意的具象泛型，这一点前文有示例。</p>
<p>假如现在有一个泛型实例，出于某种需求，我们想知道构建这个泛型实例需要用什么泛型参数。比如某人创建了一个 <code>List<T></code> 泛型的实例，并把它作为参数传给了我们的一个方法：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">var myList = newList<int>();
ShowGenericArguments(myList);</pre>
<p>我们的方法签名是这样的：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public void ShowGenericArguments(object o)</pre>
<p>这时，作为此方法的编写者，我们并不知道这个 o 对象具体是用什么类型的泛型参数构建的。通过反射，我们可以得到泛型实例的很多信息，其中最简单的就是判断一个类型是不是泛型：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public void ShowGenericArguments(object o)
&#123;
    if (o == null) return;
    Type t =o.GetType();
    if (!t.IsGenericType) return;
    ...
&#125;</pre>
<p>由于 <code>List<></code> 本身也是泛型，所以上面的判断不严谨，我们需要知道的是对象是不是一个构造泛型（<code>List<int></code>）。而 Type 类还提供了一些有用的属性：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">typeof(List<>).IsGenericType // true
typeof(List<>).IsGenericTypeDefinition // true
typeof(List<>).IsConstructedGenericType// false

typeof(List<int>).IsGenericType // true
typeof(List<int>).IsGenericTypeDefinition // false
typeof(List<int>).IsConstructedGenericType// true</pre>
<p><code>IsConstructedGenericType</code> 和 <code>IsGenericTypeDefinition</code> 分别用来判断某个泛型是不是构造泛型和非构造泛型。</p>
<p>再结合 Type 的 <code>GetGenericArguments()</code> 方法，就可以很容易地知道某个泛型实例是用什么泛型参数构建的了，例如：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">static void ShowGenericArguments(object o)
&#123;
    if (o == null) return;
    Type t = o.GetType();
    if (!t.IsConstructedGenericType) return;
    foreach (Type genericTypeArgument in t.GetGenericArguments())
        Console.WriteLine(genericTypeArgument.Name);
&#125;</pre>
<p>以上是关于反射的干货知识，都是从实际项目开发中总结而来，希望对你的开发有帮助。</p>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            