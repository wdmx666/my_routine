
#### GA-173 bug 分析

GA-173 bug 描述：将激光采集结点放置在振动台上连续振动会出现激光断续，而期望输出
是在连续异常情况下，应当连续打出激光，不应出现激光断续。

分析策略与思路：<1> 全流程检查法；<2> 根据先验知识，提出可能点验证。采用拟合或
假设检验的思路提出原假设(模型)。


![](.protocol_images\a818cc17.png)




![](.protocol_images\test.png)




为了将该问题定位，首先根据应用的基本组成对bug进行分割定位。因为激光控制与声音无关，
因此，首先将与声音相关的部分隔离。而干预系统由计算部分和执行部分组成，首先以此为结
点进行划分。


``` Python
import pandas as pd

class TestClass:
    def __init__(self):
        print("GOod")
```

![](.protocol_images\bd9723df.png)

你好

![](.protocol_images\44aa62ad.png)

![](.protocol_images\52373602.png)

![](.protocol_images\f613ed1e.png)

![](.protocol_images\a818cc17.png)

![](.protocol_images\485961ff.png)

```java
class App{
    public static void main(String[] args){
       System.out.println("Hello Markdown!")
    }
}
```

$$
a>2
$$

![test2](.protocol_images\test2.jpg)

what is wrong ？
danent
