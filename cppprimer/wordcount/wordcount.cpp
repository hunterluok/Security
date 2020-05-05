#include<algorithm>
#include<limits>
#include<string>
#include "stdint.h"
#include "hadoop/Pipes.hh"
#include "haddop/TemplateFactory.hh"
#include "hadoop/StringUtils.hh"
using namespace std;


class WordCountMapper:public HadoopPipes::Mapper
{
public:
    WordCountMapper(HadoopPipes::TaskContext& context){}
    void map(HadoopPipes::MapContext& context)
    {
        string line =context.getInputValue();
        vector<string>word = HadoopUtils::splitString(line, " ");
        for (unsigned int i=0; i<word.size(); i++)
        {
            context.emit(word[i],HadoopUtils::toString(1));
        }
    }
};
 
class WordCountReducer:public HadoopPipes::Reducer
{
public:
    WordCountReducer(HadoopPipes::TaskContext& context){}
    void reduce(HadoopPipes::ReduceContext& context)
    {
        int count = 0;
        while (context.nextValue())
        {
            count +=HadoopUtils::toInt(context.getInputValue());
        }
        context.emit(context.getInputKey(),HadoopUtils::toString(count));
    }
};
 
int main(int argc, char **argv)
{
    return HadoopPipes::runTask(HadoopPipes::TemplateFactory<WordCountMapper,WordCountReducer>());
}

