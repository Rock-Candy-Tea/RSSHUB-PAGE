
---
title: 'Java调用TensorFlow'
categories: 
    - 社交媒体
    - 知乎 - 用户文章
author: 知乎 - 用户文章
comments: false
date: Mon, 19 Jan 1970 12:17:23 GMT
thumbnail: ''
---

<div>   
<h2><b>前述</b></h2><p>最近在做一个视觉方面的Demo。坑当然是多到不行，想到这都是了解生态的一个过程，也就不那么烦躁。我们的模型训练部分往往是用Python写Keras或者直接上TensorFlow，然后得到model。但部署这件事还没听说直接用Python就能解决，大多需要别的工具。</p><p>第一种方式是通过网络，以服务器、客户端的形式实现。这时候可以写个简单的Flask接口就可以实现建议的模型部署，稍复杂、专业一些就可以用到TF Serving之类的专门的部署工具。很容易理解，这种方式使用模型的服务必须联网，由于是一些视觉方面的应用，对网络的要求可能还比较高。</p><p>第二种方式是本地化部署，将模型打包在App中直接在本地调用。App一般情况下都不是Python开发，更可能是JS、Swift、C++、Java等其他语言（TF支持JS、Swift、C/C++、Java、Go等等）。这种方式的最大缺陷就是受到设备计算资源的限制，但在我的Demo中勉强能够使用。最终也是选择了这种方式。</p><h2><b>部署原理</b></h2><p>详细来说，这篇是使用Java调用Python训练的模型。首先第一个坑，Java目前好像只支持TensorFlow1，所以Python训练也不能使用TensorFlow2。简单来说，这个部署过程就是将h5、checkpoint格式的model转成pb格式的model。在Java中只能读取pb格式的model。</p><h2><b>格式转换工具</b></h2><p>转换格式一般采用Python脚本，推荐使用pyenv保持同Java TF版本一致的Python版本及TF版本（曾因版本不同出现过莫名的问题）。<a href="https://link.zhihu.com/?target=https%3A//www.tensorflow.org/install/pip" class=" wrap external" target="_blank" rel="nofollow noreferrer">关于TF的安装</a></p><p>如果使用Keras，推荐使用<a href="https://link.zhihu.com/?target=https%3A//github.com/amir-abdi/keras_to_tensorflow" class=" wrap external" target="_blank" rel="nofollow noreferrer">keras_to_tensorflow</a>。</p><div class="highlight"><pre><code class="language-text"># ReadMe中有使用方法
# python keras_to_tensorflow.py 
#     --input_model="path/to/keras/model.h5" 
#     --input_model_json="path/to/keras/model.json" 
#     --output_model="path/to/save/model.pb"

# h5文件通过save_weights保存
model.save_weights('model.h5')
# json文件通过to_json得到
with open("model.json", "w") as json_file:
  json_file.write(model.to_json())</code></pre></div><p>如果使用TensorFlow，可以使用<a href="https://link.zhihu.com/?target=https%3A//github.com/r1cebank/tf-ckpt-2-pb" class=" wrap external" target="_blank" rel="nofollow noreferrer">tf-ckpt-2-pb</a>。</p><div class="highlight"><pre><code class="language-text"># ReadMe中的Usage
# python convert.py
#     --checkpoint "path/to/tf/ckpt_weight"
#     --model "path/to/tf/ckpt_weight/model.ckpt.meta"
#     --out-path "path/to/save/out.pb"

# checkpoint是ckpt文件夹
tf.train.Saver().save(session, path)
# mdoel是ckpt文件夹中的meta文件</code></pre></div><h2><b>找出model的input和output</b></h2><p>Java调用TF model需要知道Input layer name和Output layer name，这时候可能需要使用tensorboard工具，自己去看网络结构。</p><div class="highlight"><pre><code class="language-text">import tensorflow as tf
from tensorflow.summary import FileWriter

sess = tf.Session()
tf.train.import_meta_graph("path/to/tf/ckpt_weight/model.ckpt.meta")
FileWriter("__tb", sess.graph)

# after run python script,
# run cmd: tensorboard --logdir __tb</code></pre></div><p>只出不入的大概就是Input layer，只入不出的很可能就是Output layer。唯一需要注意的是将名称写全，比如有仅一层的名字<code>input</code>，也有几层的名字<code>generator/MODEL/outLayer</code>。</p><h2><b>Java调用TensorFlow的方法</b></h2><p>得到pb文件、Input layer name和Output layer name就只差写Java代码调用啦。<a href="https://link.zhihu.com/?target=https%3A//www.tensorflow.org/install/lang_java" class=" wrap external" target="_blank" rel="nofollow noreferrer">安装 Java 版 TensorFlow</a></p><p>这时候按照官方教程走，应该不会出什么问题。教程中现在用的是1.14.0的版本，所以python中也最好用1.14.0版本的TF。版本问题前面就已经提到过，不多说。</p><div class="highlight"><pre><code class="language-text"><dependency>
  <groupId>org.tensorflow</groupId>
  <artifactId>tensorflow</artifactId>
  <version>1.14.0</version>
</dependency></code></pre></div><p>简易的载入模型和预测函数及使用：</p><div class="highlight"><pre><code class="language-text"># TensorFlowUtils.java
public final class TensorFlowUtils &#123;
    public static Session loadModel(String modelPath, Class<?> cls) &#123;
        try &#123;
            Graph graph = new Graph();
            Session session = new Session(graph);
            graph.importGraphDef(IOUtils.toByteArray(cls.getResourceAsStream(modelPath)));
            return session;
        &#125; catch (IOException e) &#123;
            e.printStackTrace();
        &#125;
        return null;
    &#125;

    public static void closeModel(Session session) &#123;
        session.close();
    &#125;

    public static Tensor<Float> predict(Tensor<Float> input, Session session, String inputName, String outputName) &#123;
        return session.runner().feed(inputName, input).fetch(outputName).run().get(0).expect(Float.class);
    &#125;
&#125;

# Main.java
public class Main &#123;
    public static void main(String[] args) &#123;
       Session session = TensorFlowUtils.loadModel("model/path", getClass());
       
       // float[][][][] originInput = may be an image, or others
       Tensor<Float> input = Tensor.create(originInput, Float.class);
       Tensor<Float> output = TensorFlowUtils.predict(input, session,
                "<your input name>", "<your output name>");
       float[][] result = output.copyTo(new float[1][2]);
       System.out.println(result[0]);

       TensorFlowUtils.closeModel(session);
    &#125;
&#125;</code></pre></div>  
</div>
            