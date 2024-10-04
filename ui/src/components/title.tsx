interface Props{
    text: string;
}
export default function Title(props: Props){
    const { text } = props;
    return (
      <h1>{text}</h1>
    );
}