
---
title: '美团App页面视图可测性改造实践'
categories: 
 - 博客
 - 美团技术团队
 - 最近更新
headimg: 'https://p0.meituan.net/travelcube/b3fb502a4c01b1f3bcef9d6bdee1b5a8487412.png'
author: 美团技术团队
comments: false
date: Wed, 28 Jul 2021 00:00:00 GMT
thumbnail: 'https://p0.meituan.net/travelcube/b3fb502a4c01b1f3bcef9d6bdee1b5a8487412.png'
---

<div>   
<h2 id="美团app的页面特点">美团App的页面特点</h2><p>对于不同的用户，美团App页面的呈现方式其实多种多样，这就是所谓的“千人千面”。以美团首页的“猜你喜欢”模块为例，针对与不同的用户有单列、Tab、双列等多种不同形式。这么多不同的页面样式需求，如果要在1天内时间内完成开发、测试、上线流程，研发团队也面临着很大的挑战。所以测试工程师就需要重度依赖自动化测试来形成快速的验收机制。</p><p><img src="https://p0.meituan.net/travelcube/b3fb502a4c01b1f3bcef9d6bdee1b5a8487412.png" alt="图1美团App首页多种页面布局样式" referrerpolicy="no-referrer"></p><h2 id="自动化测试实施中的技术挑战">自动化测试实施中的技术挑战</h2><p>接下来，本文将会从页面元素无法定位、Appium元素定位的原理、AccessibilityNodeInfo和Drawable等三个维度进行阐述。</p><h3 id="页面元素无法定位">页面元素无法定位</h3><p><img src="https://p0.meituan.net/travelcube/e9828cf0a3dfa7090dbf8634b0c80ddb40788.png" alt="图2 页面元素审查情况" referrerpolicy="no-referrer"></p><p>目前，美团App客户端自动化主要依托于Appium（一个开源、跨平台的测试框架，可以用来测试原生及混合的移动端应用）来实现页面元素的定位和操作，当我们通过Appium Inspector进行页面元素审查时，能通过元素审查找到的信息只有外面的边框和下方的两个按钮，其他信息均无法识别(如上图2所示)。中央位置的图片、左上角的文本信息都无法通过现有的UI自动化方案进行定位和解析。不能定位元素，也就无法进行页面的操作和断言，这就严重影响了自动化的实施工作。</p><p>经过进一步的调研，我们发现这些页面卡片中大量使用Drawable对象来绘制页面的信息，从而导致元素无法进行定位。为什么Drawable对象无法定位呢？下面我们一起研究一下UI自动化元素定位的原理。</p><h3 id="appium元素定位的原理">Appium元素定位的原理</h3><p>目前的UI自动化测试，使用Appium进行页面元素的定位和操作。如下图所示，AppiumServer和UiAutomator2的手机端进行通信后完成元素的操作。</p><p><img src="https://p0.meituan.net/travelcube/94c2fdd1a91576a70d67e61dae724b5e84069.png" alt="图3 Appium的通信原理" referrerpolicy="no-referrer"></p><p>通过阅读Appium源码发现完成一次定位的流程如下图所示：</p><p><img src="https://p0.meituan.net/travelcube/29f6cbb2eab601df480f5d27b182300050750.png" alt="图4 Appium定位元素的实现流程" referrerpolicy="no-referrer"></p><ul><li>首先，Appium通过调用<code>findElement</code>的方式进行元素定位。</li><li>然后，调用Android提供<code>UIDevice</code>对象的<code>findObject</code>方法。</li><li>最终，通过<code>PartialMatch.accept</code>完成元素的查找。</li></ul><p>接下来我们看一下，这个<code>PartialMatch.accept</code>到底是如何完成元素定位的。通过对于<a href="https://android.googlesource.com/platform/frameworks/uiautomator/+/android-support-test/src/main/java/android/support/test/uiautomator/ByMatcher.java">源码</a>的研究，我们发现元素的信息都是存储在一个叫做<code>AccessibilityNodeInfo</code>的对象里面。源码中使用大量<code>node.getXXX</code>方法中的信息，大家是否眼熟呢？这些信息其实就是我们日常自动化测试中可以获取UI元素的属性。</p><p><img src="https://p0.meituan.net/travelcube/27d287ee42436a920901bc184cfd69d725211.png" alt="图5 AppiumInspector审查元素获取信息示意" referrerpolicy="no-referrer"></p><p><code>Drawable</code>无法获取元素信息，是否和<code>AccessibilityNodeInfo</code>相关？我们进一步探究<code>Drawable</code>和<code>AccessibilityNodeInfo</code>的关系。</p><h3 id="accessibilitynodeinfo和drawable">AccessibilityNodeInfo和Drawable</h3><p>通过对于源码的研究，我们绘制了如下类图来解释<code>AccessibilityNodeInfo</code>和<code>Drawable</code>之间的关系。</p><p><img src="https://p0.meituan.net/travelcube/44e4855dc8de4abe17465e2136bed6d692365.png" alt="图6 类关系示意图" referrerpolicy="no-referrer"></p><p><code>View</code>实现了<code>AccessibilityEventSource</code>接口并实现了一个叫做<code>onInitializeAccessibilityNodeInfo</code>的方法来填充信息。我们也在<a href="https://developer.android.com/guide/topics/ui/accessibility/custom-views?hl=zh-cn">Android官方文档</a>中找到了对于此信息的说明：</p><blockquote><p>onInitializeAccessibilityNodeInfo() ：此方法为无障碍服务提供有关视图状态的信息。默认的<code>View</code>实现具有一组标准的视图属性，但如果您的自定义视图提供除了简单的 <code>TextView</code>或<code>Button</code>之外的其他互动控件，则您应替换此方法并将有关视图的其他信息设置到由此方法处理的<code>AccessibilityNodeInfo</code>对象中。</p></blockquote><p>而<code>Drawable</code>并没有实现对应的方法，所以也就无法被自动化测试找到。探究了元素查找原理之后，我们就要开始着手解决问题了。</p><h2 id="页面视图可测性改造-xraysdk">页面视图可测性改造-XraySDK</h2><h3 id="定位方案对比">定位方案对比</h3><p>既然知道了<code>Drawable</code>没有填充<code>AccessibilityNodeInfo</code>，也就说明我无法接入目前的自动化测试方案来完成页面内容的获取。那我们可以想到如下三种方案来解决问题：</p><table><thead><tr><th>实现方案</th><th>影响范围</th></tr></thead><tbody><tr><td>改造Appium定位方式，让Drawable可以被识别</td><td>需要改动底层的AccessibilityNodeInfo obtain(View,int)方法和为Drawable添加AccessibilityNodeInfo这样就需要对于所有的Android系统做兼容，影响范围过大</td></tr><tr><td>使用View替代Drawable</td><td>动态布局卡片使用Drawable进行绘制就是因为Drawable比View使用资源更少，绘制性能更好，放弃使用Drawable就等于放弃了性能的改进</td></tr><tr><td>使用图像识别进行定位</td><td>动态卡片中有很多图像中包含文字，还有多行文本都会对图像识别的准确性带来很大的影响</td></tr></tbody></table><p>上面的三种方案，目前看来都无法有效地解决动态卡片元素定位的问题。如何在影响范围较小的前提下，达成获取视图信息的目标呢？接下来，我们将进一步研究动态布局的实现方案。</p><h3 id="视图信息的获取和存储-xraydumper">视图信息的获取和存储-XrayDumper</h3><p>我们的应用场景非常明确，自动化测试通过集成Client来获得和客户端交互能力，通过Client向App发送指令来页面信息的获取。那我们可以考虑内嵌一个SDK（XraySDK）来完成视图的获取，然后再向自动化提供一个客户端（XrayClient）来完成这部分功能。</p><p><img src="https://p0.meituan.net/travelcube/be15715976df10ef128432891f7488bd18021.png" alt="图7 XraySDK的工作流程示意图" referrerpolicy="no-referrer"></p><p>对于XraySDK的功能划分，如下表所示：</p><table><thead><tr><th>模块名</th><th>功能划分</th><th>运行环境</th><th>产品形态</th></tr></thead><tbody><tr><td>Xray-Client</td><td>1.和Xray-Server进行交互进行指令发送和数据的接收<br>2.暴露对外的Api给自动化或者其他系统</td><td>自动化内部或者三方系统内部</td><td>JAR包或基于其他语言的依赖包</td></tr><tr><td>Xray-SDK</td><td>1.进行页面信息的获取以及结构化(Xray-Dumper)<br>2.接收用户指令来进行结构化数据输出(Xray-Server)</td><td>App内部</td><td>客户端SDK（AAR和Pod-Library）</td></tr></tbody></table><p>XraySDK如何才能获取到我们需要的Drawable信息呢？我们先来研究一下动态布局的实现方案。</p><p><img src="https://p1.meituan.net/travelcube/c1398d7af80f42d0302e25ad8babdab832893.png" alt="图8 动态卡片的页面绘制流程" referrerpolicy="no-referrer"></p><p>动态布局的视图呈现过程分为：解析模板->绑定数据->计算布局->页面绘制，计算布局结束后，元素在页面上的位置就已经确定了，那么只要拦截这个阶段信息就可以实现视图信息的获取。</p><p>通过对于代码的研究，我们发现在<code>com.sankuai.litho.recycler.AdapterCompat</code>这个类中控制着视图布局行为，在<code>bindViewHolder</code>中完成视图的最终的布局和计算。首先，我们通过在此处插入一个自定义的监听器来拦截布局信息。</p><pre><code>public final void bindViewHolder(BaseViewHolder<Data> viewHolder, int position) &#123;
        if (viewHolder != null) &#123;
            viewHolder.bindView(context, getData(position), position);

            //自动化测试回调
            if (componentTreeCreateListeners != null) &#123;
                if (viewHolder instanceof LithoViewHolder) &#123;
                    DataHolder holder = getData(position);
                    //获取视图布局信息
                    LithoView view = ((LithoViewHolder<Data>) viewHolder).lithoView;
                    LayoutController layoutController = ((LithoDynamicDataHolder) holder).getLayoutController(null);
                    VirtualNodeBase node = layoutController.viewNodeRoot;
                    //通过监听器将视图信息向外传递给可测性SDK
                    componentTreeCreateListeners.onComponentTreeCreated(node, view.getRootView(), view.getComponentTree());
                &#125;
            &#125;
        &#125;
    &#125;
</code></pre><p>然后，通过暴露一个静态方法给可测性SDK，完成监听器的初始化。</p><pre><code>public static void setComponentTreeCreateListener(ComponentTreeCreateListener l) &#123;
        AdapterCompat.componentTreeCreateListeners = l;
        try &#123;
            // 兼容mbc的动态布局自动化测试，为避免循环依赖，采用反射调用
            Class<?> mbcDynamicClass = Class.forName("com.sankuai.meituan.mbc.business.item.dynamic.DynamicLithoItem");
            Method setComponentTreeCreateListener = mbcDynamicClass.getMethod("setComponentTreeCreateListener", ComponentTreeCreateListener.class);
            setComponentTreeCreateListener.invoke(null, l);

        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;

        try &#123;
            // 搜索新框架动态布局自动化测试
            Class<?> searchDynamicClass = Class.forName("com.sankuai.meituan.search.result2.model.DynamicItem");
            Method setSearchComponentTreeCreateListener = searchDynamicClass.getMethod("setComponentTreeCreateListener", ComponentTreeCreateListener.class);
            setSearchComponentTreeCreateListener.invoke(null, l);
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
</code></pre><p>最后，自动化通过设置自定义的监听器来完成视图信息的获取和存储。</p><pre><code>//通过静态方法设置一个ComponentTreeCreateListener来监听布局事件
AdapterCompat.setComponentTreeCreateListener(new AdapterCompat.ComponentTreeCreateListener() &#123;
            @Override
            public void onComponentTreeCreated(VirtualNodeBase node, View rootView, ComponentTree tree) &#123;
                //将信息存储到一个自定义的ViewInfoObserver对象中
                ViewInfoObserver vif = new ViewInfoObserver();
                vif.update(node, rootView, tree);
            &#125;
        &#125;);
</code></pre><p>我们将视图信息存储在ViewInfoObserver这样一个对象中。</p><pre><code>public class ViewInfoObserver implements AutoTestObserver&#123;
    public static HashMap<String, View> VIEW_MAP = new HashMap<>();
    public static HashMap<VirtualNodeBase, View> VIEW = new HashMap<>();
    public static HashMap<String, ComponentTree> COMPTREE_MAP = new HashMap<>();
    public static String uri = "http://dashboard.ep.dev.sankuai.com/outter/dynamicTemplateKeyFromJson";

    @Override
    public void update(VirtualNodeBase vn, View view,ComponentTree tree) &#123;
        if (null != vn && null != vn.jsonObject) &#123;
            try &#123;
                String string = vn.jsonObject.toString();
                Gson g = new GsonBuilder().setPrettyPrinting().create();
                JsonParser p = new JsonParser();
                JsonElement e = p.parse(string);

                String templateName = null;
                String name1 = getObject(e,"templateName");
                String name2 = getObject(e,"template_name");
                String name3 = getObject(e,"template");
                templateName = null != name1 ? name1 : (null != name2 ? name2 : (null != name3 ? name3 : null));

                if (null != templateName) &#123;
                //如果已经存储则更新视图信息
                    if (VIEW_MAP.containsKey(templateName)) &#123;
                        VIEW_MAP.remove(templateName);
                    &#125;
                    //存储视图编号
                    VIEW_MAP.put(templateName, view);
                    if (VIEW.containsKey(templateName)) &#123;
                        VIEW.remove(templateName);
                    &#125;
                    //存储视图信息
                    VIEW.put(vn, view);
                    if (COMPTREE_MAP.containsKey(templateName)) &#123;
                        COMPTREE_MAP.remove(templateName);
                    &#125;
                    COMPTREE_MAP.put(templateName, tree);
                    System.out.println("autotestDyn：update success");

                &#125;

            &#125; catch (Exception e) &#123;
                System.out.println(e.toString());
                System.out.println("autotestDyn：templateName not exist!");
            &#125;
        &#125;
    &#125;
</code></pre><p>当需要查询这些信息的时候，就可以通过XrayDumper来完成信息的输出。</p><pre><code>public class SubViewInfo &#123;
    public JSONObject getOutData(String template) throws JSONException &#123;
        JSONObject outData = new JSONObject();
        JSONObject componentTouchables = new JSONObject();

        if (!COMPTREE_MAP.isEmpty() && COMPTREE_MAP.containsKey(template) && null != COMPTREE_MAP.get(template)) &#123;
            ComponentTree cpt = COMPTREE_MAP.get(template);
            JSONArray componentArray = new JSONArray();

            ArrayList<View> touchables = cpt.getLithoView().getTouchables();
            LithoView lithoView = cpt.getLithoView();
            int[] ls = new int[2];
            lithoView.getLocationOnScreen(ls);
            int pointX = ls[0];
            int pointY = ls[1];

            for (int i = 0; i < touchables.size(); i++) &#123;
                JSONObject temp = new JSONObject();
                int height = touchables.get(i).getHeight();
                int width = touchables.get(i).getWidth();
                int[] tl = new int[2];
                touchables.get(i).getLocationOnScreen(tl);
                temp.put("height",height);
                temp.put("width",width);
                temp.put("pointX",tl[0]);
                temp.put("pointY",tl[1]);

                String url = "";
                try &#123;
                    EventHandler eh = (EventHandler) getValue(getValue(touchables.get(i), "mOnClickListener"), "mEventHandler");
                    DynamicClickListener listener = (DynamicClickListener) getValue(getValue(eh, "mHasEventDispatcher"), "listener");
                    Uri clickUri = (Uri) getValue(listener, "uri");
                    if (null != clickUri) &#123;
                        url = clickUri.toString();
                    &#125;
                &#125; catch (Exception e) &#123;
                    Log.d("autotest", "get click url error!");
                &#125;

                temp.put("url",url);
                componentArray.put(temp);
            &#125;
            componentTouchables.put("componentTouchables",componentArray);
            componentTouchables.put("componentTouchablesCount", cpt.getLithoView().getTouchables().size());

            View[] root = (View[])getValue(cpt.getLithoView(),"mChildren");
            JSONArray allComponentArray = new JSONArray();
            if (root.length > 0) &#123;
                for (int i = 0; i < root.length; i++) &#123;
                    try &#123;
                        if (null != root[i]) &#123;
                            Object items[] = (Object[]) getValue(getValue(root[i], "mMountItems"), "mValues");
                            componentTouchables.put("componentCount", items.length);
                            for (int itemIndex = 0; itemIndex < items.length; itemIndex++) &#123;
                                getMountItems(allComponentArray, items[itemIndex], pointX, pointY);
                            &#125;
                        &#125;
                    &#125; catch (Exception e) &#123;

                    &#125;
                &#125;
            &#125;
            componentTouchables.put("componentUntouchables",allComponentArray);
        &#125; else &#123;
            Log.d("autotest","COMPTREE_MAP is null!");
        &#125;
        outData.put(template,componentTouchables);
        System.out.println(outData);
        return outData;
    &#125;
    &#125;
&#125;
</code></pre><h3 id="视图信息的输出-xrayserver">视图信息的输出-XrayServer</h3><p>我们获取到了信息，接下来就要考虑如何将视图信息传递给自动化测试脚本，我们参考了Appium的设计。</p><p>Appium通过在手机上安装的InstrumentsClient启动了一个SocketServer通过HTTP协议来完成自动化和底层测试框架的数据通信。我们也可以借鉴上述思路，在美团App中启动一个WebServer来完成信息的输出。</p><p>第一步，我们实现了一个继承了Service组件，这样就可以方便的通过命令行的方式的启动和停止可测性的功能。</p><pre><code>public class AutoTestServer extends Service  &#123;
    @Override
    public IBinder onBind(Intent intent) &#123;
        return null;
    &#125;

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) &#123;
    ....
        return super.onStartCommand(intent, flags, startId);
    &#125;
&#125;
</code></pre><p>第二步，通过HttpServer的方式对外暴露通信的接口。</p><pre><code>public class AutoTestServer extends Service  &#123;
    @Override
    public IBinder onBind(Intent intent) &#123;
        return null;
    &#125;

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) &#123;
        // 创建对象，端口通过参数传入
        if (intent != null) &#123;
            int randNum = intent.getIntExtra("autoTestPort",8999);
            HttpServer myServer = new HttpServer(randNum);
            try &#123;
                // 开启HTTP服务
                myServer.start();
                System.out.println("AutoTestPort:" + randNum);
            &#125; catch (IOException e) &#123;
                System.err.println("AutoTestPort:" + e.getMessage());
                myServer = new HttpServer(8999);
                try &#123;
                    myServer.start();
                    System.out.println("AutoTestPort:8999");
                &#125; catch (IOException e1) &#123;
                    System.err.println("Default:" + e.getMessage());
                &#125;
            &#125;
        &#125;
        return super.onStartCommand(intent, flags, startId);
    &#125;
&#125;
</code></pre><p>第三步，将之前设置好的监听器进行注册。</p><pre><code>public class AutoTestServer extends Service  &#123;
    @Override
    public IBinder onBind(Intent intent) &#123;
        return null;
    &#125;

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) &#123;
    //注册监听器
        AdapterCompat.setComponentTreeCreateListener(new AdapterCompat.ComponentTreeCreateListener() &#123;
            @Override
            public void onComponentTreeCreated(VirtualNodeBase node, View rootView, ComponentTree tree) &#123;
                ViewInfoObserver vif = new ViewInfoObserver();
                vif.update(node, rootView, tree);
            &#125;
        &#125;);

        // 创建对象，端口通过参数传入
        .....
        return super.onStartCommand(intent, flags, startId);
    &#125;
&#125;
</code></pre><p>最后，在HttpServer中通过不同的路径来实现接收不同的指令。</p><pre><code>private JSONObject getResponseByUri(@Nonnull IHTTPSession session) throws JSONException &#123;
        String uri = session.getUri();
        if (isFindCommand(uri)) &#123;
            return getResponseByFindUri(uri);
        &#125;
&#125;

@Nonnull
private JSONObject getResponseByFindUri(@Nonnull String uri) throws JSONException &#123;
    String template = uri.split("/")[2];
    String protocol = uri.split("/")[3];
    switch (protocol) &#123;
        case "frame":
            TemplateLayoutFrame tlf = new TemplateLayoutFrame();
            return tlf.getOutData(template);
        case "subview":
            SubViewInfo svi = new SubViewInfo();
            return svi.getOutData(template);
        //省略了部分的代码处理逻辑    
        ....
        default:
            JSONObject errorJson = new JSONObject();
            errorJson.put("success", false);
            errorJson.put("message", "输入find链接地址有误");
            return errorJson;
    &#125;
&#125;
</code></pre><h3 id="sdk整体功能结构">SDK整体功能结构</h3><p>自动化脚本通过访问设备的特定端口（例如：<a href="http://localhost:8899/find/subview%EF%BC%89%EF%BC%8C%E7%BB%8F%E7%94%B1XrayServer%EF%BC%8C%E9%80%9A%E8%BF%87%E8%AE%BF%E9%97%AE%E8%B7%AF%E5%BE%84%E5%B0%86%E8%AF%B7%E6%B1%82%E8%BD%AC%E5%8F%91%E8%87%B3XrayDumper%E8%BF%9B%E8%A1%8C%E4%BF%A1%E6%81%AF%E7%9A%84%E6%8F%90%E5%8F%96%E5%92%8C%E8%BE%93%E5%87%BA%E3%80%82%E7%84%B6%E5%90%8E%E5%B8%83%E5%B1%80%E8%A7%A3%E6%9E%90%E5%99%A8%E5%B0%86%E5%B8%83%E5%B1%80%E4%BF%A1%E6%81%AF%E5%BA%8F%E5%88%97%E5%8C%96%E6%88%90JSON%E6%95%B0%E6%8D%AE%EF%BC%8C%E5%86%8D%E7%BB%8F%E7%94%B1XrayServer%EF%BC%8C%E9%80%9A%E8%BF%87%E7%BD%91%E7%BB%9C%E4%BB%A5HTTP%E5%93%8D%E5%BA%94%E7%9A%84%E6%96%B9%E5%BC%8F%E4%BC%A0%E5%88%B0%E7%BB%99%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%84%9A%E6%9C%AC%E3%80%82">http://localhost:8899/find/subview），经由XrayServer，通过访问路径将请求转发至XrayDumper进行信息的提取和输出。然后布局解析器将布局信息序列化成JSON数据，再经由XrayServer，通过网络以HTTP响应的方式传到给自动化测试脚本。</a></p><p><img src="https://p0.meituan.net/travelcube/0686b4d2a1bd6d9dc1855634c470c5bd203337.png" alt="图9-XraySDK功能结构示意图" referrerpolicy="no-referrer"></p><h3 id="视图信息的增强">视图信息的增强</h3><p>除了常规的位置、内容、类型等信息，我们还通过检查时间监听器的方式，进一步判断视图元素是否可以进行交互，进一步增强了页面视图结构的有效信息。</p><pre><code>// setGestures
ArrayList<String> gestures = new ArrayList<>();
if (view.isClickable())&#123;
   gestures.add("isClickable");
&#125;
if (view.isLongClickable())&#123;
   gestures.add("isLongClickable");
&#125;
//省略部分代码
.....
</code></pre><h3 id="动态布局自动化的收益">动态布局自动化的收益</h3><p>基于视图可测性的提升，美团动态化卡片的自动化测试覆盖度有了大幅的提升，从原来无法做自动化测试，到目前80%以上的动态化卡片都实现了自动化测试，而且效率也得到了明显的提升。</p><p><img src="https://p0.meituan.net/travelcube/55ba8423378be711bf7ad73b6d589cc668434.png" alt="图10 自动化效率提升收益" referrerpolicy="no-referrer"></p><h2 id="未来展望">未来展望</h2><p>页面视图信息作为客户端测试最基础且重要的属性之一，是对用户视觉信息的一种代码级的表示。它对于机器识别页面元素信息有着非常重要的作用，对于它的可测性改造将会给技术团队带来很大的收益。我们会列举了几个视图可测性改造的探索方向，仅供大家参考。</p><h3 id="使用视图解析原理解决webview元素定位">使用视图解析原理解决WebView元素定位</h3><p>应用同样的思想，我们还可以用来解决WebView元素定位的问题。</p><p><img src="https://p0.meituan.net/travelcube/144bffaa8553a3d65f6a8c7e4913f868257457.png" alt="图11 WebView页面示例" referrerpolicy="no-referrer"></p><p>通过运行在App内部的SDK，可以获取到对应的WebView实例。通过获取到根节点，从根节点开始进行循环遍历，同时把每个节点的信息存储下来就可以得到所有的视图信息了。</p><p>在WebView是否也有同样合适的根节点呢？基于对于HTML的理解我们可以想到HTML中所有的标签都是挂在BODY标签下面的，BODY标签就是我们需要选取的根节点。我们可以通过WebElement[“attrName”]的方式来进行属性的获取。</p><p><img src="https://p0.meituan.net/travelcube/9c59bc97c2dc90071b6c0812edc2b548141543.png" alt="图12 遍历WebView节点的代码示例" referrerpolicy="no-referrer"></p><h3 id="视图可测性改造的更多应用场景">视图可测性改造的更多应用场景</h3><ul><li><strong>提升功能测试可靠性</strong>：在功能测试自动化中，通过内部更加稳定和迅速的视图信息输出，可以有效提升自动化测试的稳定性。避免由于元素无法获取或者元素获取缓慢导致的自动化测试失败。</li><li><strong>提升可靠性测试效率</strong>：对于依靠随机或者按照视图信息进行页面随机操作的可靠性测试，依赖对于视图信息的过滤，也可以只操作可以交互的元素（通过过滤元素事件监听器是否为空）。这样就可以有效提升可靠性测试的效率，在单位时间内可以完成更多页面的检测。</li><li><strong>增加兼容性测试检测手段</strong>：在页面兼容性方面，通过对页面组件位置信息和属性来扫描页面内是否存在不合理的堆叠、空白区域、形状异常等UI呈现异常。也可以获取内容信息，例如图片、文本，来检查是否存在不适宜内容呈现。可以作为图像对比方案的有效补充。</li></ul><h2 id="招聘信息">招聘信息</h2><p>美团平台质量技术中心，负责美团 App 业务和大前端（移动客户端和Web前端）基础技术质量工作，沉淀流程规范和配套工具、提升研发效率。团队技术一流、氛围良好，感兴趣的同学简历可以发送至: zhangjie63@meituan.com</p>  
</div>
            