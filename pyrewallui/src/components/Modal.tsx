import React, { createContext, useContext } from "react";

interface IModalContext {
    closeModal: () => void;
}

const ModalContext = createContext<IModalContext | undefined>(undefined);
ModalContext.displayName = 'ModalContext';

interface ModalProps {
    show: boolean;
    children?: React.ReactNode;
    closeModal: () => void;
    bgClassName?: string;
    className?: string;
    innerClassName?: string;
}

export const Modal: React.FC<ModalProps> = (props) => {
    const context: IModalContext = {
        closeModal: props.closeModal
    }
    return <>
        <ModalContext.Provider value={context}>
            <div className={`bg-black/70 fixed top-0 left-0 w-screen h-screen outline-none z-50 overflow-hidden ${props.show ? 'block':'hidden'} ${props.bgClassName}`} onClick={props.closeModal}>
                <div className={`relative pointer-events-none mx-auto mt-0 lg:mt-20 z-50 w-200 ${props.className}`} onClick={(e) => { e.stopPropagation(); }}>
                    <div className={`shadow-lg relative flex flex-col w-200 pointer-events-auto bg-white bg-clip-padding outline-none ${props.innerClassName}`}>
                        {props.children}
                    </div>
                </div>
            </div>
        </ModalContext.Provider>
    </>
}

interface ModalComponentProps extends React.HTMLAttributes<HTMLElement> {}

interface ModalHeaderProps extends ModalComponentProps {
    optionButtons?: React.ReactNode;
}

export const ModalHeader: React.FC<ModalHeaderProps> = (props) => {
    const { closeModal } = useContext(ModalContext)!;
    const { className, children, optionButtons, ...otherProps } = props;

    return <>
        <div className={`flex flex-shrink-0 items-center justify-between px-4 py-3 bg-slate-700 ${className}`} {...otherProps}>
            <h5 className={`text-xl font-medium leading-normal text-white`} {...otherProps}>{children}</h5>
            {optionButtons}
            <button type="button" className="box-content w-4 h-4 text-white border-none rounded-none focus:shadow-none focus:outline-none hover:text-slate-300 hover: opacity-75 hover:no-underline" aria-label="Close" onClick={closeModal}>X</button>
        </div>
    </>;
}

export const ModalBody: React.FC<ModalComponentProps> = (props) => {
    const { className, children, ...otherProps } = props;
    return <div className={`relative p-4 max-h-full ${className}`} {...otherProps}>{children}</div>;
}

export const ModalFooter: React.FC<ModalComponentProps> = (props) => {
    const { className, children, ...otherProps } = props;

    return <div className={`flex flex-shrink-0 flex-wrap items-center justify-end px-4 py-2 ${className}`} {...otherProps}>
          {children}
    </div>;
};